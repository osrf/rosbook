# BEGIN ALL
#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist

cmd_vel_pub = rospy.Publisher('cmd_vel', Twist, queue_size=1) #<1>
rospy.init_node('red_light_green_light')

red_light_twist = Twist() #<2>
green_light_twist = Twist()
green_light_twist.linear.x = 0.5 #<3>

driving_forward = False
light_change_time = rospy.Time.now()
rate = rospy.Rate(10)

while not rospy.is_shutdown():
  if driving_forward:
    cmd_vel_pub.publish(green_light_twist) #<4>
  else:
    cmd_vel_pub.publish(red_light_twist)
  # BEGIN PART_1
  if rospy.Time.now() > light_change_time: #<5>
    driving_forward = not driving_forward
    light_change_time = rospy.Time.now() + rospy.Duration(3)
  # END PART_1
  rate.sleep() #<6>
# END ALL
