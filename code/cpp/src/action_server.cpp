#include <ros/ros.h>
#include <actionlib/server/simple_action_server.h>
#include <cpp/SampleAction.h>

actionlib::SimpleActionServer<cpp::SampleAction> *g_action_server = NULL;

void sample_action_callback(const cpp::SampleGoalConstPtr &goal)
{
  // do stuff
  cpp::SampleResult result;
  g_action_server->setSucceeded(result);
}

int main(int argc, char **argv) {
  ros::init(argc, argv, "action_server");
  ros::NodeHandle node;

  actionlib::SimpleActionServer<cpp::SampleAction> server(
    node, "sample_action", sample_action_callback, false);
  g_action_server = &server;
  server.start();

  ros::spin();
  
  return 0;
}
