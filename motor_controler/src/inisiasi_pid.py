
#!/usr/bin/env python

from __future__ import print_function

import sys
import rospy
from motor_controler.srv import *

def set_awal_PID(p, i, d, setpoint):
    rospy.wait_for_service('set_pid')
    try:
        set_PID = rospy.ServiceProxy('set_pid', PID)
        resp1 = set_PID(p, i, d, setpoint)
        return resp1.sum
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)

def usage():
    return "%s [p i d setpoint]"%sys.argv[0]

if __name__ == "__main__":
    if len(sys.argv) == 5:
        p = float(sys.argv[1])
        i = float(sys.argv[2])
        d = float(sys.argv[3])
        setpoint = float(sys.argv[4])
    else:
        print(usage())
        sys.exit(1)

    print("P[%.2f], I[%.2f], D[%.2f], set point[%.2f]"%(p, i, d, setpoint))
    print("Calculation output = %.2f"%(set_awal_PID(p, i, d, setpoint)))