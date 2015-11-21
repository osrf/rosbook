#!/usr/bin/env python

import math, time
import rospy
from std_msgs.msg import Float64

rospy.init_node('cosine_wave')
pub = rospy.Publisher('cos', Float64)
while not rospy.is_shutdown():
  msg = Float64()
  msg.data = math.cos(4*time.time())
  pub.publish(msg)
  time.sleep(0.1)
