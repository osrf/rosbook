#!/usr/bin/env python

import rospy
from smach import StateMachine # <1>
from smach_ros import SimpleActionState # <2>
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal

waypoints = [
    ['one', (2.1, 2.2), (0.0, 0.0, 0.0, 1.0)],
    ['two', (6.5, 4.43), (0.0, 0.0, -0.984047240305, 0.177907360295)]
]


if __name__ == '__main__':
    patrol = StateMachine('success')
    with patrol:
        for i,w in enumerate(waypoints):
            goal_pose = MoveBaseGoal()
            goal_pose.target_pose.header.frame_id = 'map'
            goal_pose.target_pose.pose.position.x = w[1][0]
            goal_pose.target_pose.pose.position.y = w[1][1]
            goal_pose.target_pose.pose.position.z = 0.0
            goal_pose.target_pose.pose.orientation.x = w[2][0]
            goal_pose.target_pose.pose.orientation.y = w[2][1]
            goal_pose.target_pose.pose.orientation.z = w[2][2]
            goal_pose.target_pose.pose.orientation.w = w[2][3]

            StateMachine.add(w[0],
                             SimpleActionState('move_base',
                                               MoveBaseAction,
                                               goal=goal_pose),
                             transitions={'success':waypoints[(i + 1) % \
                               len(waypoints)][0]})

    patrol.execute()
    
