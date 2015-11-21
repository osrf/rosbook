#include <ros/ros.h> // <1>


int main(int argc, char **argv) {
  ros::init(argc, argv, "minimal");  // <2>
  ros::NodeHandle n;  // <3>

  ros::spin();  // <4>

  return 0;
}
