#!/usr/bin/env python3

"""
Script that tests a simple color thresholding vision approach.

Example usage:
  Python:   python3 test_vision.py --min_h 0 --max_h 30 --min_s 220 --max_s 255 --min_v 0 --max_v 255
  ros2:     ros2 run tb3_autonomy test_vision.py --min_h 0 --max_h 30 --min_s 220 --max_s 255 --min_v 0 --max_v 255

For reference, these are some approximate thresholds on the H channel.
  Red: 160 - 180
  Green: 40 - 90
  Blue: 100 - 150

Since the blocks are highly saturated, the default S channel thresholds are tight (220-255)
"""

import argparse
import cv_bridge
import cv2
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image


class ColorThresholdTester(Node):
    def __init__(self, args):
        # Define ROS subscriber
        super().__init__("test_vision")
        self.sub = self.create_subscription(
            Image, "/image_raw", self.img_callback, 10
        )

        # Define vision related variables
        self.bridge = cv_bridge.CvBridge()
        cv2.namedWindow("Image with Detections", cv2.WINDOW_NORMAL)
        params = cv2.SimpleBlobDetector_Params()
        params.minArea = 100
        params.maxArea = 100000
        params.filterByArea = True
        params.filterByColor = False
        params.filterByInertia = False
        params.filterByConvexity = False
        params.thresholdStep = 60
        self.detector = cv2.SimpleBlobDetector_create(params)
        self.min_bounds = (args.min_h, args.min_s, args.min_v)
        self.max_bounds = (args.max_h, args.max_s, args.max_v)
        self.get_logger().info(
            f"Using limits:\n"
            f"H: [{args.min_h} {args.max_h}] "
            f"S: [{args.min_s} {args.max_s}] "
            f"V: [{args.min_v} {args.max_v}] "
        )

    def img_callback(self, msg):
        """Image topic subscriber callback"""
        img = self.bridge.imgmsg_to_cv2(msg, desired_encoding="bgr8")
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, self.min_bounds, self.max_bounds)
        keypoints = self.detector.detect(mask)
        labeled_img = cv2.drawKeypoints(
            img,
            keypoints,
            None,
            (255, 0, 0),
            cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS,
        )
        cv2.imshow("Image with Detections", labeled_img)
        cv2.waitKey(10)


if __name__ == "__main__":
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="HSV Color Thresholding test script")
    parser.add_argument("--min_h", type=int, default=0)
    parser.add_argument("--max_h", type=int, default=255)
    parser.add_argument("--min_s", type=int, default=220)
    parser.add_argument("--max_s", type=int, default=255)
    parser.add_argument("--min_v", type=int, default=0)
    parser.add_argument("--max_v", type=int, default=255)
    args = parser.parse_args()

    # Start ROS node and subscriber
    rclpy.init()
    subscriber = ColorThresholdTester(args)
    rclpy.spin(subscriber)
    subscriber.destroy_node()
    rclpy.shutdown()
