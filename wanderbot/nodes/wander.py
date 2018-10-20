#!/usr/bin/env python

# Sends movement commands to the Turtlebot 3
# The turtlebot3 can be observed in Gazebo by running: roslaunch turtlebot3_gazebo turtlebot3_empty_world.launch

import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan


g_range_ahead = 1.0

def scan_callback(msg):
    global g_range_ahead
    g_range_ahead = min(msg.ranges)
    

scan_sub = rospy.Subscriber('scan', LaserScan, scan_callback)
cmd_vel_pub = rospy.Publisher('cmd_vel', Twist, queue_size=1)
rospy.init_node('wander')

# Wait for the first clock message to be published
while not rospy.get_rostime():
    pass

driving_forward = True
state_change_time = rospy.Time.now() + rospy.Duration(3)
rate = rospy.Rate(10)

while not rospy.is_shutdown():
    if driving_forward:
        print g_range_ahead
        if g_range_ahead < 0.3 or rospy.get_rostime() > state_change_time:
            driving_forward = False
            print 'Stop driving'
            state_change_time = rospy.Time.now() + rospy.Duration(5)
    else:
        if rospy.Time.now() > state_change_time:
            driving_forward = True
            print 'driving forward'
            state_change_time = rospy.Time.now() + rospy.Duration(5)

    twist = Twist()
    if driving_forward:
        twist.linear.x = 0.3
    else:
        twist.angular.z = 1
    cmd_vel_pub.publish(twist)

    rate.sleep()
