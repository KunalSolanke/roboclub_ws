#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import String

def test() :
    rospy.init_node("chatter",anonymous=True)
    rate = rospy.Rate(10)
    

    while not rospy.is_shutdown() :
        hello_str = "Hello Kunal" 
        rospy.loginfo(hello_str)
        rate.sleep()


if __name__ == '__main__' :
    try:
        test()
    except rospy.ROSInterruptException :
                pass 
