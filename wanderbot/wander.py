#!/usr/bin/env python
# BEGIN ALL
import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

def scan_callback(msg):
  global g_range_ahead
  g_range_ahead = min(msg.ranges)

g_range_ahead = 1 # anything to start
scan_sub = rospy.Subscriber('scan', LaserScan, scan_callback)
cmd_vel_pub = rospy.Publisher('cmd_vel', Twist, queue_size=1)
rospy.init_node('wander')
state_change_time = rospy.Time.now()
driving_forward = True
rate = rospy.Rate(10)

while not rospy.is_shutdown():
  if driving_forward:
    # BEGIN FORWARD
    if (g_range_ahead < 0.8 or rospy.Time.now() > state_change_time):
      driving_forward = False
      state_change_time = rospy.Time.now() + rospy.Duration(5)
    # END FORWARD
  else: # we're not driving_forward
    # BEGIN TURNING
    if rospy.Time.now() > state_change_time:
      driving_forward = True # we're done spinning, time to go forwards!
      state_change_time = rospy.Time.now() + rospy.Duration(30)
    # END TURNING
  twist = Twist()
  if driving_forward:
    twist.linear.x = 1
  else:
    twist.angular.z = 1
  cmd_vel_pub.publish(twist)

  rate.sleep()
# END ALL
