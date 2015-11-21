#! /usr/bin/env python
import rospy

import actionlib
from basics.msg import TalkAction, TalkGoal, TalkResult

rospy.init_node('speaker_client')
client = actionlib.SimpleActionClient('speak', TalkAction)
client.wait_for_server()
goal = TalkGoal()
goal.sentence = "hello world, hello world, hello world, hello world"
client.send_goal(goal)
client.wait_for_result()
print('[Result] State: %d'%(client.get_state()))
print('[Result] Status: %s'%(client.get_goal_status_text()))
