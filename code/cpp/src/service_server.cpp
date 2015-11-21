#include <ros/ros.h>
#include <cpp/WordCount.h>


bool count(cpp::WordCount::Request &req,  // <1>
	   cpp::WordCount::Response &res) {
  l = strlen(req.words);
  if (l == 0)
    count = 0;
  else {
    count = 1;
    for(int i = 0; i < l; ++i)
      if (req.words[i] == ' ')
	++count;
  }

  res.count = count;

  return true;
}


int main(int argc, char **argv) {
  ros::init(int argc, char **argv, "count_server");
  ros::NodeHandle node;

  ros::ServiceServer service = node.advertiseService("count", count);  // <2>

  ros::spin();  // <3>


  return 0;
}
