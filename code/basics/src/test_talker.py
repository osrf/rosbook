#!/usr/bin/env python

import sys, unittest, time
import rospy, rostest
from std_msgs.msg import String

class TestTalker(unittest.TestCase):

    def __init__(self, *args):
        super(TestTalker, self).__init__(*args)
        self.success = False

    def callback(self, data):
        self.success = data.data and data.data.startswith('hello world')

    def test_talker(self):
        rospy.init_node('test_talker')
        rospy.Subscriber("chatter", String, self.callback)
        timeout_t = time.time() + 10.0
        while (not rospy.is_shutdown() and
               not self.success and time.time() < timeout_t):
            time.sleep(0.1)
        self.assert_(self.success)

if __name__ == '__main__':
    rostest.rosrun('basics', 'talker_test', TestTalker, sys.argv)
