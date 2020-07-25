#!/usr/bin/env python
# license removed for brevity

import rospy 
from std_msgs.msg import Float32 
import random
def publisher() :
    pub  = rospy.Publisher("my_random_float_python",Float32,queue_size=10)
    rospy.init_node("publisher_python",anonymous= True) 
    rate =rospy.Rate(10) 
    random_float = Float32() 
    while not rospy.is_shutdown() :
        random_float.data = random.random()*10.0 
        pub.publish(data=random_float.data)
        rospy.loginfo("I am publishing {}".format(random_float.data)) 
        rate.sleep()



if __name__ == '__main__' :
    try :
        publisher() 
    except rospy.ROSInterruptException :
       pass 

    
