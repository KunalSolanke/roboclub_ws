#include "ros/ros.h"
#include<sstream>
#include<string>
#include "std_msgs/String.h"
#include<iostream>
int main(int argc,char **argv){
	ros::init(argc,argv,"chatter_c") ;
	ros::NodeHandle chatter_c ;
        ROS_INFO("Hello Kunal") ;
	std::cout<<"Hello Kunal"<<"\n" ;
/*	ros::Publisher chatter_pub = node.advertise<std_msgs::String>("chatter_c",100) ;
	ros::Rate loop_rate(10) ;

	while(ros::ok()){
		std_msgs::String msg ;
		std::stringstream name ;
		name<<"Kunal Solanke" ;
		msg.data = name.str() ;
		ROS_INFO("Hello %s",msg.data.c_str()) ;
		chatter_pub.publish(msg) ;
		ros::spinOnce() ;
		loop_rate.sleep() ;
	}    */
	return 0 ;
}

