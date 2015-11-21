#!/usr/bin/env python
import sys, rospy, tf, moveit_commander, random
from geometry_msgs.msg import Pose, Point, Quaternion

class R2ChessboardWrapper:
  def __init__(self):
    self.left_arm = moveit_commander.MoveGroupCommander("left_arm")

  def setPose(self, x, y, z, phi, theta, psi):
    orient = \
      Quaternion(*tf.transformations.quaternion_from_euler(phi, theta, psi))
    pose = Pose(Point(x, y, z), orient)
    self.left_arm.set_pose_target(pose)
    self.left_arm.go(True)

  def setSquare(self, square, height_above_board):
    if len(square) != 2 or not square[1].isdigit():
      raise ValueError(
        "expected a chess rank and file like 'b3' but found %s instead" %
        square)
    rank_y = -0.3 - 0.05 * (ord(square[0]) - ord('a'))
    file_x =  0.5 - 0.05 * int(square[1])
    z = float(height_above_board) + 1.0
    self.setPose(file_x, rank_y, z, 3.14, 0.3, -1.57)

if __name__ == '__main__':
  moveit_commander.roscpp_initialize(sys.argv)
  rospy.init_node('r2_chessboard_cli')
  argv = rospy.myargv(argv=sys.argv) # filter out any arguments used by ROS
  if len(argv) != 3:
    print "usage: r2_chessboard.py square height"
    sys.exit(1)
  r2w = R2ChessboardWrapper()
  r2w.setSquare(*argv[1:])
  moveit_commander.roscpp_shutdown()
