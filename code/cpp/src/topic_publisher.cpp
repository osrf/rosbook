#include <ros/ros.h>
#include <std_msgs/Int32.h>  // <1>


int main(int argc, char **argv) {
  ros::init(argc, argv, "count_publisher");
  ros::NodeHandle node;

  ros::Publisher pub = node.advertise<std_msgs::Int32>("counter", 10); // <2>

  ros::Rate rate(1);  // <3>
  int count = 0;

  while (ros::ok()) {  // <4>
    std_msgs::Int32 msg; // <5>
    msg.data = count;

    pub.publish(msg);  // <6>

    ++count;
    rate.sleep();  // <7>
  }

  return 0;  // <8>
}
