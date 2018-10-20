#!/usr/bin/env python

# A node that acts both as a publisher and a subscriber
# Use case:
# In one terminal, listen:          rostopic echo /doubled
# In another terminal, publish:     rostopic pub /number std_msgs/Int32 -1 10

import rospy
from std_msgs.msg import Int32

rospy.init_node('doubler')

def callback(msg):
    doubled = Int32()
    doubled.data = msg.data * 2
    pub.publish(doubled)


sub = rospy.Subscriber('number', Int32, callback)
pub = rospy.Publisher('doubled', Int32, queue_size=20)

rospy.spin()
