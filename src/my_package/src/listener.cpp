#include "ros/ros.h"
#include<iostream>
#include <bits/stdc++.h> 
#include "std_msgs/Float32.h"

std_msgs::Float32 my_float ;
void RandomFloatCallback(const std_msgs::Float32::ConstPtr& random_float){
        my_float.data =std::log(random_float->data);
	 ROS_INFO("Received : %f,Publishing:%f ",random_float->data,my_float.data) ;

}

int main(int argc ,char **argv){
	ros::init(argc,argv,"subscriber") ;
	ros::NodeHandle subscriber ;
	ros::Publisher pub = subscriber.advertise<std_msgs::Float32>("random_float_log",1000) ;
	ros::Subscriber sub = subscriber.subscribe("my_random_float",10,RandomFloatCallback) ;
	pub.publish(my_float);
	ros::spin() ;
	return 0 ;

}
