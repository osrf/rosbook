#!/usr/bin/env python
import sys, rospy, tf, actionlib, moveit_commander
from geometry_msgs.msg import *
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from tf.transformations import quaternion_from_euler
from control_msgs.msg import (GripperCommandAction, GripperCommandGoal)

if __name__ == '__main__':
  moveit_commander.roscpp_initialize(sys.argv)
  rospy.init_node('deliver_to_counter')
  args = rospy.myargv(argv=sys.argv)
  gripper = actionlib.SimpleActionClient("gripper_controller/gripper_action",
    GripperCommandAction)
  gripper.wait_for_server()
  move_base = actionlib.SimpleActionClient('move_base', MoveBaseAction)
  move_base.wait_for_server()
  goal = MoveBaseGoal()
  goal.target_pose.header.frame_id = 'map'
  goal.target_pose.pose.position.x = 4
  orient = Quaternion(*quaternion_from_euler(0, 0, 0))
  goal.target_pose.pose.orientation = orient
  move_base.send_goal(goal)
  move_base.wait_for_result()

  arm = moveit_commander.MoveGroupCommander("arm")
  arm.allow_replanning(True)
  p = Pose()
  p.position.x = 0.9
  p.position.z = 0.95
  p.orientation = Quaternion(*quaternion_from_euler(0, 0.5, 0))
  arm.set_pose_target(p)
  arm.go(True)
  gripper_goal = GripperCommandGoal()
  gripper_goal.command.max_effort = 10.0
  gripper_goal.command.position = 0.15
  gripper.send_goal(gripper_goal)
  gripper.wait_for_result(rospy.Duration(1.0))

  p.position.x = 0.05
  p.position.y = -0.15
  p.position.z = 0.75
  p.orientation = Quaternion(*quaternion_from_euler(0, -1.5, -1.5))
  arm.set_pose_target(p)
  arm.go(True)

  goal.target_pose.pose.position.x = 0
  move_base.send_goal(goal)
  move_base.wait_for_result()
