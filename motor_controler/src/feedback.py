#!/usr/bin/env python

import rospy
from sensor_msgs.msg import NavSatFix
from geometry_msgs.msg import TwistStamped
from nav_msgs.msg import Odometry

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

def odometry_callback(data):
	position_x = data.pose.pose.position.x
	position_y = data.pose.pose.position.y
	position_z = data.pose.pose.position.z
	orientation_x = data.pose.pose.orientation.x
	orientation_y = data.pose.pose.orientation.y
	orientation_z = data.pose.pose.orientation.z
	orientation_w = data.pose.pose.orientation.w

	print("Position: x={}, y={}, z={}".format(position_x, position_y, position_z))
	print("Orientation: x={}, y={}, z={}, w={}".format(orientation_x, orientation_y, orientation_z, orientation_w))
    

if __name__ == '__main__':
	rospy.init_node('feedback_pid', anonymous=True)
	rospy.Subscriber('/mavros/global_position/global', NavSatFix, navsatfix_callback)
	rospy.Subscriber('/mavros/local_position/velocity', TwistStamped, twiststamped_callback)
	rospy.Subscriber('mavros/local_position/odom', Odometry, odometry_callback)
	rospy.spin()
	
	
