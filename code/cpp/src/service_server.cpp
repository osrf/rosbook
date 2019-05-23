#include <ros/ros.h>
#include <cpp/WordCount.h>


bool count(cpp::WordCount::Request &req,  // <1>
	   cpp::WordCount::Response &res) {
  const size_t l = strlen(req.words.c_str());
  if (l == 0)
    res.count = 0;
  else {
    res.count = 1;
    for(size_t i = 0; i < l; ++i)
      if (req.words[i] == ' ')
        res.count++;
  }

  return true;
}


int main(int argc, char **argv) {
  ros::init(argc, argv, "count_server");
  ros::NodeHandle node;

  ros::ServiceServer service = node.advertiseService("count", count);  // <2>

  ros::spin();  // <3>

  return 0;
}
