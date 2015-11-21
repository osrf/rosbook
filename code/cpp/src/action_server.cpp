#include <ros/ros.h>
#include <actionlib/server/simple_action_server.h>
#include <cpp/MyAction.h>


int main(int argc, char **argv) {
  ros::init(argc, argv, "action_server");
  ros::NodeHandle node;

  actionlib::SimpleActionServer<cpp::MyAction> server;
  cpp::MyActionFeedback feedback;
  cpp::MyActionResult result;

  
  return 0;
}
