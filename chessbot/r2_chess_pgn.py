#!/usr/bin/env python
import sys, rospy, tf, moveit_commander, random
from geometry_msgs.msg import Pose, Point, Quaternion
import pgn

class R2ChessboardPGN:
  def __init__(self):
    self.left_arm = moveit_commander.MoveGroupCommander("left_arm")
    self.left_hand = moveit_commander.MoveGroupCommander("left_hand")

  def setGrasp(self, state):
    if state == "pre-pinch":
      vec = [ 0.3, 0, 1.57, 0,  # index
              -0.1, 0, 1.57, 0, # middle
              0, 0, 0,          # ring
              0, 0, 0,          # pinkie
              0, 1.1, 0, 0]       # thumb
    elif state == "pinch":
      vec = [ 0, 0, 1.57, 0,
              0, 0, 1.57, 0,
              0, 0, 0,
              0, 0, 0,
              0, 1.1, 0, 0]
    elif state == "open":
      vec = [0] * 18
    else:
      raise ValueError("unknown hand state: %s" % state)
    self.left_hand.set_joint_value_target(vec)
    self.left_hand.go(True)

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
    print "going to %s" % square
    rank_y = -0.24 - 0.05 * int(square[1])
    file_x =  0.5 - 0.05 * (ord(square[0]) - ord('a'))
    z = float(height_above_board) + 1.0
    self.setPose(file_x, rank_y, z, 3.14, 0.3, -1.57)

  def playGame(self, pgn_filename):
    game = pgn.loads(open(pgn_filename).read())[0]
    self.setGrasp("pre-pinch")
    self.setSquare("a1", 0.15)
    for move in game.moves:
      self.setSquare(move[0:2], 0.10)
      self.setSquare(move[0:2], 0.015)
      self.setGrasp("pinch")
      self.setSquare(move[0:2], 0.10)
      self.setSquare(move[2:4], 0.10)
      self.setSquare(move[2:4], 0.015)
      self.setGrasp("pre-pinch")
      self.setSquare(move[2:4], 0.10)

if __name__ == '__main__':
  moveit_commander.roscpp_initialize(sys.argv)
  rospy.init_node('r2_chess_pgn',anonymous=True)
  argv = rospy.myargv(argv=sys.argv) # filter out any arguments used by ROS
  if len(argv) != 2:
    print "usage: r2_chess_pgn.py PGNFILE"
    sys.exit(1)
  print "playing %s" % argv[1]
  r2pgn = R2ChessboardPGN()
  r2pgn.playGame(argv[1])
  moveit_commander.roscpp_shutdown()
