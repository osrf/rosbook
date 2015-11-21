#!/usr/bin/env python
# BEGIN ALL
import rospy
from sensor_msgs.msg import Image
import cv2, cv_bridge
from geometry_msgs.msg import Twist

class Follower:
  def __init__(self):
    self.bridge = cv_bridge.CvBridge()
    cv2.namedWindow("window", 1)
    self.image_sub = rospy.Subscriber('camera/rgb/image_raw', 
                                      Image, self.image_callback)
    self.cmd_vel_pub = rospy.Publisher('cmd_vel_mux/input/teleop',
                                       Twist, queue_size=1)
    self.twist = Twist()
  def image_callback(self, msg):
    image = self.bridge.imgmsg_to_cv2(msg)
    cv2.imshow("window", image)
    cv2.waitKey(3)
    #self.twist.linear.x = 0.2
    #self.cmd_vel_pub.publish(self.twist)

rospy.init_node('follower')
follower = Follower()
rospy.spin()
# END ALL
