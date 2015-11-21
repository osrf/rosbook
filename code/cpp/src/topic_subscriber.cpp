#include <ros/ros.h>
#include <std_msgs/Int32.h>

#include <iostream>


void callback(const std_msgs::Int32::ConstPtr &msg) {  // <1>
  std::cout << msg->data << std::endl;
}


int main(int argc, char **argv) {
  ros::init(argc, argv, "count_subscriber");
  ros::NodeHandle node;

  ros::Subscriber sub = node.subscribe("counter", 10, callback);  // <2>

  ros::spin();
}

