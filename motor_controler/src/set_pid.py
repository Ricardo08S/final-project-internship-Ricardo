#!/usr/bin/env python

from __future__ import print_function

from motor_controler.srv import PID, PIDResponse
import rospy

class PIDs:
    def __init__(self, p, i, d, set_point):
        self._p = p
        self._i = i
        self._d = d
        self._set_point = set_point

        self.last_error = 0
        self.last_time = 0
        self.integral_cumulation = 0
        self.current_feedback = 0

        self.use_time = False
        self.use_output_bound = False
        self.use_max_i_cum = False

    def calculation(self):
        current_error = self._set_point - self.current_feedback
        if self.use_time:
            delta_time = self.current_time - self.last_time
            cycle_integral = (self.last_error + current_error / 2) * delta_time
            self.integral_cumulation += cycle_integral
            cycle_derivative = (current_error - self.last_error) / delta_time
            self.last_time = self.current_time
        else:
            self.integral_cumulation += current_error
            cycle_derivative = current_error - self.last_error

        if self.use_max_i_cum:
            if self.integral_cumulation > self.max_integral_comulation:
                self.integral_cumulation = self.max_integral_comulation
            elif self.integral_cumulation < -self.max_integral_comulation:
                self.integral_cumulation = -self.max_integral_comulation

        output = (current_error * self._p) + (self.integral_cumulation * self._i) + (cycle_derivative * self._d)
        if self.use_output_bound:
            if output > self.output_upper_bound:
                output = self.output_upper_bound
            elif output < self.output_lower_bound:
                output = self.output_lower_bound

        self.last_error = current_error
        return output

    def getP(self):
        return self._p

    def getI(self):
        return self._i

    def getD(self):
        return self._d

    def getPropotional(self):
        return self.current_error * self._p

    def getIntegral(self):
        return self.integral_cumulation * self._i

    def getDerivative(self):
        return self.cycle_derivative * self._d

    def getIntegralCum(self):
        return self.integral_cumulation

    def setP(self, p):
        self._p = p

    def setI(self, i):
        self._i = i

    def setD(self, d):
        self._d = d

    def setTarget(self, set_point):
        self._set_point = set_point

    def setPID(self, p, i, d):
        self._p = p
        self._i = i
        self._d = d

    def setFeedback(self, feedback):
        self.current_feedback = feedback

    def setTime(self, time):
        self.current_time = time

    def setMaxIntegralCum(self, max_integral_cum):
        self.max_integral_comulation = max_integral_cum

    def setOutputBound(self, lower_bound, upper_bound):
        self.output_lower_bound = lower_bound
        self.output_upper_bound = upper_bound

pid = PIDs(0.0, 0.0, 0.0, 0)


def settle_PID(req):
    pid.setP(req.p)
    pid.setI(req.i)
    pid.setD(req.d)
    pid.setTarget(req.s)
    print("Returning set P[%.2f], I[%.2f], D[%.2f], set point[%.2f]" %(req.p, req.i, req.d, req.s))
    return PIDResponse(pid.calculation())

def set_pid_server():
    rospy.init_node('set_pid_server')
    rospy.Service('set_pid', PID, settle_PID)
    print("Ready to set PID.")
    rospy.spin()

if __name__ == "__main__":
    set_pid_server()
    