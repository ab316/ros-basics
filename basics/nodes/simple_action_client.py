#!/usr/bin/env python

# Simple action client that sends a 5 second wait goal to the simple action server

import actionlib
import rospy
from basics.msg import TimerAction, TimerGoal

rospy.init_node('timer_action_client')
client = actionlib.SimpleActionClient('timer', TimerAction)
client.wait_for_server()

goal = TimerGoal()
goal.time_to_wait = rospy.Duration.from_sec(5.0)
client.send_goal(goal)
client.wait_for_result()

print 'Time elapsed: %f' % client.get_result().time_elapsed.to_sec()
