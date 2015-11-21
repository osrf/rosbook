#!/usr/bin/env python
import sys, rospy, tf, actionlib
from geometry_msgs.msg import *
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from tf.transformations import quaternion_from_euler
from tf.transformations import euler_from_quaternion
from control_msgs.msg import PointHeadAction, PointHeadGoal

class BinDocker:
  def __init__(self):
    self.move_base = actionlib.SimpleActionClient('move_base', MoveBaseAction)
    self.move_base.wait_for_server()
    self.tf_listener = tf.TransformListener()
    self.head_client = actionlib.SimpleActionClient("head_controller/point_head", PointHeadAction)
    self.head_client.wait_for_server()
  def point_head_forwards(self):
    goal = PointHeadGoal()
    goal.target.header.stamp = rospy.Time.now()
    goal.target.header.frame_id = "base_link"
    goal.target.point.x = 0.7
    goal.target.point.y = 0
    goal.target.point.z = 0.5
    goal.min_duration = rospy.Duration(1.0)
    self.head_client.send_goal(goal)
    self.head_client.wait_for_result()
  def dock(self, target_bin):
    self.target_bin = target_bin
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
      marker_frame = "ar_marker_%d_up" % self.target_bin
      try:
        t = self.tf_listener.getLatestCommonTime("/base_link", marker_frame)
        print "age: %.6f" % (rospy.Time.now() - t).to_sec()
        if (rospy.Time.now() - t).to_sec() > 0.2:
          rospy.sleep(0.1)
          continue
        (marker_translation, marker_orient) = self.tf_listener.lookupTransform('/base_link',marker_frame,t)
        print "marker: " + str(marker_translation)
        target_translation = Vector3(1.3, 0, 0.5)
        if (abs(marker_translation[0]) + abs(marker_translation[1])) < 0.15:
          print "close enough!"
          break;
        goal = MoveBaseGoal()
        goal.target_pose.header.frame_id = marker_frame
        goal.target_pose.pose.position.x = 0
        goal.target_pose.pose.position.y = -1.5
        orient = Quaternion(*quaternion_from_euler(0, 0, 1.57))
        goal.target_pose.pose.orientation = orient
        self.move_base.send_goal(goal)
        self.move_base.wait_for_result()
        result = self.move_base.get_result()
        nav_state = self.move_base.get_state()
        if nav_state == 3:
          print "move success! waiting to calm down before looking again..."
          rospy.sleep(1) # wait for things to calm down a bit before looking
          self.point_head_forwards()
          rospy.sleep(0.5)
          print "done waiting."
        else:
          print "move failure!"

      except(tf.Exception, tf.LookupException, 
             tf.ConnectivityException, tf.ExtrapolationException):
        rate.sleep() # not yet in view

if __name__ == '__main__':
  rospy.init_node('dock_with_bin')
  args = rospy.myargv(argv=sys.argv)
  if len(args) != 2:
    print "usage: dock_with_bin.py BIN_NUMBER"
    sys.exit(1)
  bd = BinDocker()
  try:
    bd.dock(int(args[1]))
  except rospy.ROSInterruptException:
    pass
