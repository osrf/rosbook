#! /usr/bin/env python
# BEGIN ALL
#! /usr/bin/env python
import rospy

import actionlib
from basics.msg import TimerAction, TimerGoal, TimerResult

rospy.init_node('timer_action_client')
# BEGIN PART_1
client = actionlib.SimpleActionClient('timer', TimerAction)
client.wait_for_server()
# END PART_1
# BEGIN PART_2
goal = TimerGoal()
goal.time_to_wait = rospy.Duration.from_sec(5.0)
client.send_goal(goal)
# END PART_2
# BEGIN PART_3
client.wait_for_result()
print('Time elapsed: %f'%(client.get_result().time_elapsed.to_sec()))
# END PART_3
# END ALL
