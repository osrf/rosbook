#!/usr/bin/env python
import sys, rospy, tf, moveit_commander, random
from geometry_msgs.msg import Pose, Point, Quaternion

class R2Hand:
  def __init__(self):
    self.left_hand = moveit_commander.MoveGroupCommander("left_hand")

  def setGrasp(self, state):
    if state == "pre-pinch":
      vec = [ 0.3, 0, 1.57, 0,  # index
              -0.1, 0, 1.57, 0, # middle
              0, 0, 0,          # ring
              0, 0, 0,          # pinkie
              0, 1.1, 0, 0]       # thumb
    elif state == "pinch":
      vec = [ -0.1, 0, 1.57, 0,
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

if __name__ == '__main__':
  moveit_commander.roscpp_initialize(sys.argv)
  rospy.init_node('r2_hand')
  argv = rospy.myargv(argv=sys.argv) # filter out any arguments used by ROS
  if len(argv) != 2:
    print "usage: r2_hand.py STATE"
    sys.exit(1)
  r2w = R2Hand()
  r2w.setGrasp(argv[1])
