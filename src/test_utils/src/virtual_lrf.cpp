#include <iostream>
#include <ros/ros.h>

int main(int argc, char** argv)
{
  std::cout << "Hellow world!"
            << "\n";

  ros::init(argc, argv, "virtual_lrf");
  ros::NodeHandle n;
  ros::Rate loop_rate(10);

  int count = 0;
  while (ros::ok())
  {
    ROS_DEBUG("log:%i", count);
    ROS_INFO("log:%i", count);
    ROS_WARN("log:%i", count);
    ROS_ERROR("log:%i", count);
    ROS_FATAL("log:%i", count);

    ros::spinOnce();
    loop_rate.sleep();
    count++;
  }
  return 0;
}
