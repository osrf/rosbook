#! /usr/bin/env python
import rospy
import threading, time, pyttsx
import actionlib
from basics.msg import TalkAction, TalkGoal, TalkResult

class TalkNode():

    def __init__(self, node_name, action_name):
        rospy.init_node(node_name)
        self.server = actionlib.SimpleActionServer(action_name, TalkAction,
          self.do_talk, False)
        self.engine = pyttsx.init()
        self.engine_thread = threading.Thread(target=self.loop)
        self.engine_thread.start()
        self.engine.setProperty('volume', rospy.get_param('~volume', 1.0))
        self.engine.setProperty('rate', rospy.get_param('~rate', 200.0))
        self.preempt = rospy.get_param('~preempt', False)
        self.server.start()

    def loop(self):
        self.engine.startLoop(False)
        while not rospy.is_shutdown():
            self.engine.iterate()
            time.sleep(0.1)
        self.engine.endLoop()
    
    def do_talk(self, goal):
        self.engine.say(goal.sentence)
        while self.engine.isBusy():
            if self.preempt and self.server.is_preempt_requested():
                self.engine.stop()
                while self.engine.isBusy():
                    time.sleep(0.1)
                self.server.set_preempted(TalkResult(), "Talk preempted")
                return
            time.sleep(0.1)
        self.server.set_succeeded(TalkResult(), "Talk completed successfully")

talker = TalkNode('speaker', 'speak')
rospy.spin()
