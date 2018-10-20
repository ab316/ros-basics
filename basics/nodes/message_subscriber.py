#!/usr/bin/env python

# A node that listens for a custom message on a topic

import rospy
from basics.msg import Complex


def callback(msg):
    print 'Real: ', msg.real
    print 'Imaginary: ', msg.imaginary


rospy.init_node('message_subscriber')
sub = rospy.Subscriber('complex', Complex, callback)
rospy.spin()
