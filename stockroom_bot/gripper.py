#!/usr/bin/env python
import sys, rospy, actionlib
from control_msgs.msg import (GripperCommandAction, GripperCommandGoal)

if __name__ == "__main__":
    rospy.init_node("gripper")
    args = rospy.myargv(argv = sys.argv)
    if len(args) != 2:
      print("usage: gripper.py GRASP_WIDTH")
      sys.exit(1)
    
    gripper = actionlib.SimpleActionClient("gripper_controller/gripper_action", GripperCommandAction)
    gripper.wait_for_server()
    rospy.loginfo("...connected.")

    gripper_goal = GripperCommandGoal()
    gripper_goal.command.max_effort = 10.0
    gripper_goal.command.position = float(args[1])

    gripper.send_goal(gripper_goal)
    gripper.wait_for_result(rospy.Duration(2.0))
    rospy.loginfo("...done")
