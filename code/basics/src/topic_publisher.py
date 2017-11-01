#!/usr/bin/env python
# BEGIN ALL
# BEGIN SHEBANG
#!/usr/bin/env python
# END SHEBANG

# BEGIN IMPORT
import rospy
# END IMPORT

# BEGIN STD_MSGS
from std_msgs.msg import Int32
# END STD_MSGS


rospy.init_node('topic_publisher')

# BEGIN PUB
pub = rospy.Publisher('counter', Int32, queue_size=10)
# END PUB

# BEGIN LOOP
rate = rospy.Rate(2)

count = 0
while not rospy.is_shutdown():
    pub.publish(count)
    count += 1
    rate.sleep()
# END LOOP
# END ALL
