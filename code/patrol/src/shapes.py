# BEGIN ALL
#!/usr/bin/env python

import rospy
from smach import State,StateMachine

from time import sleep


class Drive(State):
    def __init__(self, distance):
        State.__init__(self, outcomes=['success'])
        self.distance = distance

    def execute(self, userdata):
        print 'Driving', self.distance
        sleep(1)
        return 'success'

class Turn(State):
    def __init__(self, angle):
        State.__init__(self, outcomes=['success'])
        self.angle = angle
        
    def execute(self, userdata):
        print 'Turning', self.angle
        sleep(1)
        return 'success'


if __name__ == '__main__':
# BEGIN PART_2
    triangle = StateMachine(outcomes=['success'])
    with triangle:
        StateMachine.add('SIDE1', Drive(1), transitions={'success':'TURN1'})
        StateMachine.add('TURN1', Turn(120), transitions={'success':'SIDE2'})
        StateMachine.add('SIDE2', Drive(1), transitions={'success':'TURN2'})
        StateMachine.add('TURN2', Turn(120), transitions={'success':'SIDE3'})
        StateMachine.add('SIDE3', Drive(1), transitions={'success':'success'})
# END PART_2

    square = StateMachine(outcomes=['success'])
    with square:
        StateMachine.add('SIDE1', Drive(1), transitions={'success':'TURN1'})
        StateMachine.add('TURN1', Turn(90), transitions={'success':'SIDE2'})
        StateMachine.add('SIDE2', Drive(1), transitions={'success':'TURN2'})
        StateMachine.add('TURN2', Turn(90), transitions={'success':'SIDE3'})
        StateMachine.add('SIDE3', Drive(1), transitions={'success':'TURN3'})
        StateMachine.add('TURN3', Turn(90), transitions={'success':'SIDE4'})
        StateMachine.add('SIDE4', Drive(1), transitions={'success':'success'})
        
# BEGIN PART_3
    shapes = StateMachine(outcomes=['success'])
    with shapes:
        StateMachine.add('TRIANGLE', triangle, transitions={'success':'SQUARE'})
        StateMachine.add('SQUARE', square, transitions={'success':'success'})

    shapes.execute()
# END PART_3
# END ALL
