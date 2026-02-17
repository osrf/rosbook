#!/usr/bin/env python3

"""
Script that tests the `navigate_to_pose` action client to move the robot base.

Example usage:
  Python:   python3 test_move_base.py --x 0 --y 2 --theta 1.57
  ros2:     ros2 run tb3_autonomy test_move_base.py --x 0 --y 2 --theta 1.57
"""

import argparse
import rclpy
from rclpy.action import ActionClient
from rclpy.node import Node
import transforms3d
from nav2_msgs.action import NavigateToPose


class MoveBaseClient(Node):
    def __init__(self):
        super().__init__("move_base_client")
        self.cli = ActionClient(self, NavigateToPose, "/navigate_to_pose")
        self.get_logger().info("Move base test node started")

    def send_pose_goal(self, x, y, theta):
        self.get_logger().info(f"Going to [x: {x}, y: {y}, theta: {theta}] ...")
        goal_msg = NavigateToPose.Goal()
        goal_msg.pose.pose.position.x = x
        goal_msg.pose.pose.position.y = y
        quat = transforms3d.euler.euler2quat(0, 0, theta)
        goal_msg.pose.pose.orientation.w = quat[0]
        goal_msg.pose.pose.orientation.x = quat[1]
        goal_msg.pose.pose.orientation.y = quat[2]
        goal_msg.pose.pose.orientation.z = quat[3]
        self.cli.wait_for_server()
        return self.cli.send_goal_async(goal_msg)


if __name__ == "__main__":
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Move base test script")
    parser.add_argument("--x", type=float, default=1.0)
    parser.add_argument("--y", type=float, default=0.0)
    parser.add_argument("--theta", type=float, default=0.0)
    args = parser.parse_args()

    # Start ROS node and action client
    rclpy.init()
    client = MoveBaseClient()

    # Send goal to the move_base action server
    future = client.send_pose_goal(args.x, args.y, args.theta)
    rclpy.spin_until_future_complete(client, future)
    client.get_logger("Pose goal reached.")
