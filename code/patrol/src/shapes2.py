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

# BEGIN PART_1
def polygon(sides):
    polygon = StateMachine(outcomes=['success'])
    with polygon:
        # Add all but the final side
        for i in xrange(sides - 1):
            StateMachine.add('SIDE_{0}'.format(i + 1),
                             Drive(1),
                             transitions={'success':'TURN_{0}'.format(i + 1)})

        # Add all the turns
        for i in xrange(sides - 1):
            StateMachine.add('TURN_{0}'.format(i + 1),
                             Turn(360.0 / sides),
                             transitions={'success':'SIDE_{0}'.format(i + 2)})

        # Add the final side
        StateMachine.add('SIDE_{0}'.format(sides),
                         Drive(1),
                         transitions={'success':'success'})

    return polygon
# END PART_1


if __name__ == '__main__':
# BEGIN PART_2
    triangle = polygon(3)
    square = polygon(4)
# END PART_2

    shapes = StateMachine(outcomes=['success'])
    with shapes:
        StateMachine.add('TRIANGLE', triangle, transitions={'success':'SQUARE'})
        StateMachine.add('SQUARE', square, transitions={'success':'success'})

    shapes.execute()
# END ALL
