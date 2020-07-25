#!/usr/bin/env python2
# license removed for brevity

import rospy 
from std_mgs.msg import Float32 
import random
def publisher() :
    pub  = rospy.Publisher("my_random_float_python",Float32,queue_size=10)
    rospy.init_node("publisher_python",anonymous= True) 
    rate =rospy.Ratte(10) 

    while not rospy.is_shutdown() :
        random_float = Float32() 
        random_float.data = random.random()*10.0 
        pub.publish(random_float)
        rospy.loginfo("I am publishing {}".format(random_float.data)) 
        rospy.spin()
        rate.sleep()



if __name__ = '__main__' :
    try :
        publisher() 
    except ROSInterrupException :
       pass 

    
