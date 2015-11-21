# BEGIN ALL
#!/usr/bin/env python

import rospy
# BEGIN PART_1
from smach import State,StateMachine
# END PART_1

from time import sleep


# BEGIN PART_2
class One(State):
    def __init__(self):
        State.__init__(self, outcomes=['success'])

    def execute(self, userdata):
        print 'one'
        sleep(1)
        return 'success'
# END PART_2

class Two(State):
    def __init__(self):
        State.__init__(self, outcomes=['success'])

    def execute(self, userdata):
        print 'two'
        sleep(1)
        return 'success'


if __name__ == '__main__':
# BEGIN PART_3
    sm = StateMachine(outcomes=['success'])
    with sm:
        StateMachine.add('ONE', One(), transitions={'success':'TWO'})
        StateMachine.add('TWO', Two(), transitions={'success':'ONE'})
        
    sm.execute()
# END PART_3
# END ALL
