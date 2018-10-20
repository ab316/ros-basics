#!/usr/bin/env python

# Client to use with the fancy action server

import time
import sys

import rospy
import actionlib
from basics.msg import TimerAction, TimerGoal, TimerResult, TimerFeedback

def feedback_cb(feedback):
    print '[Feedback] Time elapsed: %f' % feedback.time_elapsed.to_sec()
    print '[Feedback] Time Remaining: %f' % feedback.time_remaining.to_sec()


def usage():
    print 'Usage: rosrun basics fancy_action_client.py DURATION [CANCEL_AFTER]'


if len(sys.argv) == 1:
    usage()
    exit(0)

if len(sys.argv) >= 2:
    wait = float(sys.argv[1])
else:
    wait = 5.0

if len(sys.argv) >= 3:
    cancel = float(sys.argv[2])
else:
    cancel = 0.0

rospy.init_node('timer_action_client')
client = actionlib.SimpleActionClient('timer', TimerAction)
client.wait_for_server()

goal = TimerGoal()
goal.time_to_wait = rospy.Duration.from_sec(wait)
client.send_goal(goal, feedback_cb=feedback_cb)

if cancel:
    time.sleep(cancel)
    client.cancel_goal()


client.wait_for_result()
print '[Result] State: %d' % client.get_state()
print '[Result] Status: %s' % client.get_goal_status_text()
print '[Result] Time Elapsed: %f' % client.get_result().time_elapsed.to_sec()
print '[Result] Updates sent: %d' % client.get_result().updates_sent
