#! /usr/bin/env python
# BEGIN ALL
#! /usr/bin/env python
import rospy

import time
import actionlib
# BEGIN PART_1
from basics.msg import TimerAction, TimerGoal, TimerResult, TimerFeedback
# END PART_1

def do_timer(goal):
    start_time = time.time()
    # BEGIN PART_2
    update_count = 0
    # END PART_2

    # BEGIN PART_3
    if goal.time_to_wait.to_sec() > 60.0:
        result = TimerResult()
        result.time_elapsed = rospy.Duration.from_sec(time.time() - start_time)
        result.updates_sent = update_count
        server.set_aborted(result, "Timer aborted due to too-long wait")
        return
    # END PART_3

    # BEGIN PART_4
    while (time.time() - start_time) < goal.time_to_wait.to_sec():
    # END PART_4

        # BEGIN PART_5
        if server.is_preempt_requested():
            result = TimerResult()
            result.time_elapsed = rospy.Duration.from_sec(time.time() - start_time)
            result.updates_sent = update_count
            server.set_preempted(result, "Timer preempted")
            return
        # END PART_5

        # BEGIN PART_6
        feedback = TimerFeedback()
        feedback.time_elapsed = rospy.Duration.from_sec(time.time() - start_time)
        feedback.time_remaining = goal.time_to_wait - feedback.time_elapsed
        server.publish_feedback(feedback)
        update_count += 1
        # END PART_6

        # BEGIN PART_7
        time.sleep(1.0)
        # END PART_7

    # BEGIN PART_8
    result = TimerResult()
    result.time_elapsed = rospy.Duration.from_sec(time.time() - start_time)
    result.updates_sent = update_count
    server.set_succeeded(result, "Timer completed successfully")
    # END PART_8

rospy.init_node('timer_action_server')
server = actionlib.SimpleActionServer('timer', TimerAction, do_timer, False)
server.start()
rospy.spin()
# END ALL
