#!/usr/bin/env python
import sys, rospy, actionlib
from control_msgs.msg import PointHeadAction, PointHeadGoal

if __name__ == '__main__':
  rospy.init_node('look_at_bin')
  head_client = actionlib.SimpleActionClient("head_controller/point_head",
    PointHeadAction)
  head_client.wait_for_server()
  goal = PointHeadGoal()
  goal.target.header.stamp = rospy.Time.now()
  goal.target.header.frame_id = "base_link"
  goal.target.point.x = 0.7
  goal.target.point.y = 0
  goal.target.point.z = 0.4
  goal.min_duration = rospy.Duration(1.0)
  head_client.send_goal(goal)
  head_client.wait_for_result()
