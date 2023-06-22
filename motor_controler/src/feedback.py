#!/usr/bin/env python

import rospy
from sensor_msgs.msg import NavSatFix
from geometry_msgs.msg import TwistStamped

def twiststamped_callback(data):

	linear_x = data.twist.linear.x
	linear_y = data.twist.linear.y
	linear_z = data.twist.linear.z

	angular_x = data.twist.angular.x
	angular_y = data.twist.angular.y
	angular_z = data.twist.angular.z

	print("TwistStamped - Linear: x={}, y={}, z={}".format(linear_x, linear_y, linear_z))
	print("TwistStamped - Angular: x={}, y={}, z={}".format(angular_x, angular_y, angular_z))

def navsatfix_callback(data):

	latitude = data.latitude
	longitude = data.longitude
	altitude = data.altitude

	print("NavSatFix - Latitude: {}".format(latitude))
	print("NavSatFix - Longitude: {}".format(longitude))
	print("NavSatFix - Altitude: {}".format(altitude))

if __name__ == '__main__':
	rospy.init_node('feedback_pid')
	rospy.Subscriber('/mavros/global_position/global', NavSatFix, navsatfix_callback)
	rospy.Subscriber('/mavros/local_position/velocity', TwistStamped, twiststamped_callback)
	rospy.spin()
	
	
