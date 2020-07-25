#!/usr/bin/env python2
# license removed for brevity
 
import rospy 
from std_mgs.msg import Float32
import random

global float_log = Float32()




def subscriber_callback(data) :
        float_log.data = data.data
        rospy.loginfo("Received Float {}  and Publisher log : {}".format(data.data,float_log.data ) 




def subscirber() :
    log_pub = rospy.Publisher("random_float_log_python",Float32,queue_size=10)
    rospy.init_node("subscriber__python",anonymous= True)
    rospy.Subscriber("my_random_float_python",Float32,subsciber_callback)
    rate =rospy.Ratte(10)

    while not rospy.is_shutdown() :

        log_pub.publish(float_log)
        rospy.spin()
        rate.sleep()



if __name__ = '__main__' :
    try :
          subscriber()
    except ROSInterrupException :
       pass

