#!/usr/bin/env python
# BEGIN ALL
import cv2, cv_bridge, numpy
from sensor_msgs.msg import Image
from geometry_msgs.msg import Twist

import sys
import termios
# import os
import yaml
import random
import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile
from nav_msgs.msg import Odometry
import time
# import py_trees
# import py_trees_ros
# from py_trees.common import OneShotPolicy
# from ament_index_python.packages import get_package_share_directory

# from tb3_behaviors.navigation import GoToPose, GetLocationFromQueue
# from tb3_behaviors.vision import LookForObject


# default_location_file = os.path.join(
#     get_package_share_directory("tb3_worlds"), "maps", "sim_house_locations.yaml"
# )

class Follower(Node):
  def __init__(self):
    super().__init__("follower_node")
    self.sub = self.create_subscription(
        Image, "/image_raw", self.img_callback, 10
    )
    self.bridge = cv_bridge.CvBridge()
    cv2.namedWindow("window", 1)
    qos = QoSProfile(depth=1)
    self.cmd_vel_pub = self.create_publisher(Twist, 'cmd_vel', qos)
    self.twist = Twist()
    
  def img_callback(self, msg):
    twist = Twist()
    img = self.bridge.imgmsg_to_cv2(msg,desired_encoding='bgr8')
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower_yellow = numpy.array([ 10,  10,  10])
    upper_yellow = numpy.array([255, 255, 250])
    mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
    
    h = int(img.shape[0])
    w = int(img.shape[1])
    d = int(img.shape[2])
    self.get_logger().info(f"img.shape [h: {h}, w: {w}, d: {d}] ...")
    search_top = 3*h/4
    search_bot = 3*h/4 + 20
    self.get_logger().info(f"search_top: {search_top}, search_bot: {search_bot}")
    mask[0:int(search_top), 0:w] = 0
    mask[int(search_bot):h, 0:w] = 0
    M = cv2.moments(mask)
    if M['m00'] > 0:
      cx = int(M['m10']/M['m00'])
      cy = int(M['m01']/M['m00'])
      cv2.circle(img, (cx, cy), 20, (0,0,255), -1)
      # BEGIN CONTROL
      err = cx - w/2
      twist.linear.x = 0.2
      twist.angular.z = -float(err) / 100
      self.cmd_vel_pub.publish(twist)
      # END CONTROL
    cv2.imshow("window", img)
    cv2.waitKey(3)

# rospy.init_node('follower')
# follower = Follower()
# rospy.spin()
# END ALL

if __name__ == "__main__":
    rclpy.init()
    follower = Follower()
    rclpy.spin(follower)
    # follower.execute()
    follower.destroy_node()
    rclpy.shutdown()

