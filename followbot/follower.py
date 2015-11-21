#!/usr/bin/env python
# BEGIN ALL
import rospy
from sensor_msgs.msg import Image

# BEGIN CALLBACK
def image_callback(msg):
  pass
  # END CALLBACK

rospy.init_node('follower')
image_sub = rospy.Subscriber('camera/rgb/image_raw', Image, image_callback)
rospy.spin()
# END ALL
