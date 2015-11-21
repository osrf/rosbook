#!/usr/bin/env python
import sys, rospy, tf, moveit_commander, random
from geometry_msgs.msg import Pose, Point, Quaternion

orient = [Quaternion(*tf.transformations.quaternion_from_euler(3.14, -1.5, -1.57)),
          Quaternion(*tf.transformations.quaternion_from_euler(3.14, -1.5, -1.57))] # <1>
pose = [Pose(Point( 0.5, -0.5, 1.3), orient[0]),
        Pose(Point(-0.5, -0.5, 1.3), orient[1])] # <2>
moveit_commander.roscpp_initialize(sys.argv) # <3>
rospy.init_node('r2_wave_arm',anonymous=True)
group = [moveit_commander.MoveGroupCommander("left_arm"),
         moveit_commander.MoveGroupCommander("right_arm")]
# now, wave arms around randomly 
while not rospy.is_shutdown():
  pose[0].position.x =  0.5 + random.uniform(-0.1, 0.1)
  pose[1].position.x = -0.5 + random.uniform(-0.1, 0.1)
  for side in [0,1]:
    pose[side].position.z =  1.5 + random.uniform(-0.1, 0.1)
    group[side].set_pose_target(pose[side])
    group[side].go(True)

moveit_commander.roscpp_shutdown()
