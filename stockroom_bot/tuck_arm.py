#!/usr/bin/env python
# modified from Fetch's prepare_simulated_robot.py 

import rospy, actionlib
from control_msgs.msg import (FollowJointTrajectoryAction,
                              FollowJointTrajectoryGoal)
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint

arm_joint_names = \
["shoulder_pan_joint", "shoulder_lift_joint", "upperarm_roll_joint", 
 "elbow_flex_joint", 
 "forearm_roll_joint", "wrist_flex_joint", "wrist_roll_joint"]
arm_intermediate_positions  = [1.32, 0, -1.4, 1.72, 0.0, 1.66, 0.0]
arm_joint_positions  = [1.32, 1.40, -0.2, 1.72, 0.0, 1.66, 0.0]

if __name__ == "__main__":
    rospy.init_node("tuck_arm")
    arm_client = actionlib.SimpleActionClient("arm_controller/follow_joint_trajectory", FollowJointTrajectoryAction)
    arm_client.wait_for_server()

    trajectory = JointTrajectory()
    trajectory.joint_names = arm_joint_names
    trajectory.points.append(JointTrajectoryPoint())
    trajectory.points[0].positions = [0.0] * len(arm_joint_positions)
    trajectory.points[0].velocities =  [0.0] * len(arm_joint_positions)
    trajectory.points[0].accelerations = [0.0] * len(arm_joint_positions)
    trajectory.points[0].time_from_start = rospy.Duration(1.0)
    trajectory.points.append(JointTrajectoryPoint())
    trajectory.points[1].positions = arm_intermediate_positions
    trajectory.points[1].velocities =  [0.0] * len(arm_joint_positions)
    trajectory.points[1].accelerations = [0.0] * len(arm_joint_positions)
    trajectory.points[1].time_from_start = rospy.Duration(4.0)
    trajectory.points.append(JointTrajectoryPoint())
    trajectory.points[2].positions = arm_joint_positions
    trajectory.points[2].velocities =  [0.0] * len(arm_joint_positions)
    trajectory.points[2].accelerations = [0.0] * len(arm_joint_positions)
    trajectory.points[2].time_from_start = rospy.Duration(7.5)

    arm_goal = FollowJointTrajectoryGoal()
    arm_goal.trajectory = trajectory
    arm_goal.goal_time_tolerance = rospy.Duration(0.0)

    arm_client.send_goal(arm_goal)
    arm_client.wait_for_result(rospy.Duration(6.0))
