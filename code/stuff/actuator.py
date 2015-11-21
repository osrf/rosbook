# BEGIN ALL
#!/usr/bin/env python

from fake_actuator import FakeActuator

import rospy
import actionlib
from std_msgs.msg import Float32

# BEGIN IMPORT
from sensors.srv import Light,LightResponse
from sensors.msg import RotationAction,RotationFeedback,RotationResult
# END IMPORT


# BEGIN TOPIC_CALLBACK
def volume_callback(msg):
    actuator.set_volume(min(100, max(0, int(msg.data * 100))))
# END TOPIC_CALLBACK


# BEGIN SERVICE_CALLBACK
def light_callback(request):
    actuator.toggle_light(request.on)
    return LightResponse(actuator.light_on())
# END SERVICE_CALLBACK


# BEGIN ACTION_CALLBACK
def rotation_callback(goal):
    feedback = RotationFeedback()
    result = RotationResult()

    actuator.set_position(goal.orientation)
    success = True

    rate = rospy.Rate(10)
    while fabs(goal.orientation - actuator.position()) > 0.01:
        if a.is_preempt_requested():
            success = False
            break;

        feedback.current_orientation = actuator.position()
        a.publish_feedback(feedback)
        rate.sleep()

    result.final_orientation = actuator.position()
    if success:
        a.set_succeeded(result)
    else:
        a.set_preempted(result)
# END ACTION_CALLBACK
    

if __name__ == '__main__':
    actuator = FakeActuator() # <1>

    # Initialize the node
    rospy.init_node('fake')

    # Topic for the volume
    t = rospy.Subscriber('fake/volume', Float32, volume_callback) # <2>

    # Service for the light
    s = rospy.Service('fake/light', Light, light_callback) # <3>

    # Action for the position
    a = actionlib.SimpleActionServer('fake/position', RotationAction, # <4>
                                     execute_cb=rotation_callback,
                                     auto_start=False)
    a.start()

    # Start everything
    rospy.spin()
# END ALL
