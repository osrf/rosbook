#!/usr/bin/env python
# BEGIN ALL
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist

key_mapping = { 'w': [ 0, 1], 'x': [0, -1], 
                'a': [-1, 0], 'd': [1,  0], 
                's': [ 0, 0] }
g_last_twist = None 
g_vel_scales = [0.1, 0.1] # default to very slow 

def keys_cb(msg, twist_pub):
  global g_last_twist, g_vel_scales
  if len(msg.data) == 0 or not key_mapping.has_key(msg.data[0]):
    return # unknown key.
  vels = key_mapping[msg.data[0]]
  g_last_twist.angular.z = vels[0] * g_vel_scales[0]
  g_last_twist.linear.x  = vels[1] * g_vel_scales[1]
  twist_pub.publish(g_last_twist)

if __name__ == '__main__':
  rospy.init_node('keys_to_twist')
  twist_pub = rospy.Publisher('cmd_vel', Twist, queue_size=1)
  rospy.Subscriber('keys', String, keys_cb, twist_pub)
  g_last_twist = Twist() # initializes to zero
  # BEGIN PARAM
  if rospy.has_param('~linear_scale'):
    g_vel_scales[1] = rospy.get_param('~linear_scale')
  else:
    rospy.logwarn("linear scale not provided; using %.1f" %\
                  g_vel_scales[1])
  # END PARAM

  if rospy.has_param('~angular_scale'):
    g_vel_scales[0] = rospy.get_param('~angular_scale')
  else:
    rospy.logwarn("angular scale not provided; using %.1f" %\
                  g_vel_scales[0])

  rate = rospy.Rate(10)
  while not rospy.is_shutdown():
    twist_pub.publish(g_last_twist)
    rate.sleep()
# END ALL
