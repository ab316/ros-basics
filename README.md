# Basics
My first attempt at learning ROS 1.0. This repository contains code/packages I made while studying the book "Programming Robots with ROS"

## Getting Started
Follow the instructions to run the package

### Prequisites
* ROS Melodic or newer
* Gazebo 9 from [http://gazebosim.org/tutorials?cat=guided_b&tut=guided_b1]
* `sudo apt-get install ros-melodic-gazebo-ros-pkgs ros-melodic-gazebo-ros-control ros-melodic-teleop-twist-keyboard`
* The Following ROS package. They can be compiled in a separate catkin workspace
  * `git clone https://github.com/ROBOTIS-GIT/turtlebot3_msgs.git`
  * `git clone https://github.com/ROBOTIS-GIT/turtlebot3.git`


### Setup     
1- Clone the repository in the src folder in your catkin workspace

2- Run `catkin_make` and `catkin_make install`

