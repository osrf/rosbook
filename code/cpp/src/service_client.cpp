#include <ros/ros.h>
#include <cpp/WordCount.h>

#include <iostream>


int main(int argc, char **argv) {
  ros::init(argc, char **argv, "count_client");
  ros::NodeHandle node;

  ros::ServiceClient client = node.serviceClient<cpp::WordCount>("count");  // <1>

  cpp::WordCount srv;  // <2>
  srv.request.words = "one two three four";

  if (client.call(srv))  // <3>
    std::cerr << "success: " << srv.response.count << std::endl;  // <4>
  else
    std::cerr << "failure" << std::endl;

  return 0;
}
