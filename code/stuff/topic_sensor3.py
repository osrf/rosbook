#!/usr/bin/env python

from math import pi
from threading import Lock

from fake_sensor import FakeSensor

import rospy
import tf

from geometry_msgs.msg import Quaternion


def make_quaternion(angle):
    q = tf.transformations.quaternion_from_euler(0, 0, angle)
    return Quaternion(*q)

def save_value(value):
    with lock: # <1>
        angle = value * 2 * pi / 100.0 # <2>
    
    
if __name__ == '__main__':
    lock = Lock() # <3>

    sensor = FakeSensor()
    sensor.register_callback(save_value)

    rospy.init_node('fake_sensor')

    pub = rospy.Publisher('angle', Quaternion, queue_size=10) 

    angle = None # <4>
    rate = rospy.Rate(10.0)
    while not rospy.is_shutdown():
        with lock:
            if angle: # <5>
                q = make_quaternion(angle)
                pub.publish(q)
        
        rate.sleep()
