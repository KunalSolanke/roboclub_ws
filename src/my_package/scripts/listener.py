#!/usr/bin/env python
# license removed for brevity
 
import rospy 
from std_msgs.msg import Float32
import random
import math

global float_log 
float_log=Float32()




def subscriber_callback(data) :
        float_log.data =math.log(data.data)
        rospy.loginfo("Received Float {}  and Publisher log : {}".format(data.data,float_log.data) ) 




def subscriber() :
    log_pub = rospy.Publisher("random_float_log_python",Float32,queue_size=10)
    rospy.init_node("subscriber_python",anonymous=True)
    rospy.Subscriber("my_random_float_python",Float32,subscriber_callback)
    log_pub.publish(float_log)
    rospy.spin()
     



if __name__ == '__main__' :
    try :
          subscriber()
    except rospy.ROSInterruptException :
       pass

