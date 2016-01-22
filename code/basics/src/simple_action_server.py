#! /usr/bin/env python
# BEGIN ALL
#! /usr/bin/env python
import rospy

# BEGIN PART_1
import time
import actionlib
from basics.msg import TimerAction, TimerGoal, TimerResult
# END PART_1

# BEGIN PART_2
def do_timer(goal):
    start_time = time.time()
    time.sleep(goal.time_to_wait.to_sec())
    # END PART_2
    # BEGIN PART_3
    result = TimerResult()
    result.time_elapsed = rospy.Duration.from_sec(time.time() - start_time)
    result.updates_sent = 0
    # END PART_3
    # BEGIN PART_4
    server.set_succeeded(result)
    # END PART_4

rospy.init_node('timer_action_server')
server = actionlib.SimpleActionServer('timer', TimerAction, do_timer, False)
server.start()
rospy.spin()
# END ALL
