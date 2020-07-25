#include "ros/ros.h"
#include<iostream>
#include<cstdlib>
#include "std_msgs/Float32.h"

int main(int argc ,char **argv){
	ros::init(argc,argv,"publisher") ;
	ros::NodeHandle publisher ;
	ros::Publisher pub = publisher.advertise<std_msgs::Float32>("my_random_float",1000) ;
	ros::Rate loop_rate(10) ;
	while(ros::ok()){
		std_msgs::Float32 random_float ;
	  random_float.data= (float)(std::rand()%100000)/10000.0 
		  ;
	  ROS_INFO("I am publishing %f",random_float.data) ;
	  pub.publish(random_float) ;
	  ros::spinOnce() ;
	  loop_rate.sleep() ;


	}
	return 0 ;

}
