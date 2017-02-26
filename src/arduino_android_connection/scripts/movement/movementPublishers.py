#!/usr/bin/env python
# Software License Agreement (BSD License)
#
# Copyright (c) 2008, Willow Garage, Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above
#    copyright notice, this list of conditions and the following
#    disclaimer in the documentation and/or other materials provided
#    with the distribution.
#  * Neither the name of Willow Garage, Inc. nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#
# Revision $Id$

## Simple talker demo that published std_msgs/Strings messages
## to the 'chatter' topic

import rospy
from std_msgs.msg import Empty

#publishes a move forward topic which will move the rover forward
def movement_moveForward():
    pub = rospy.Publisher('movement/moveForward', Empty, queue_size=10)
    if(not rospy.is_shutdown()):
        rospy.loginfo("moving forward" + str(rospy.get_time()))
        pub.publish()

#publishes a move forward topic which will move the rover backward
def movement_moveBackward():
    pub = rospy.Publisher('movement/moveBackward', Empty, queue_size=10)
    if(not rospy.is_shutdown()):
        rospy.loginfo("moving backward" + str(rospy.get_time()))
        pub.publish()

#publishes a move forward topic which will turn the rover left
def movement_turnLeft():
    pub = rospy.Publisher('movement/turnLeft', Empty, queue_size=10)
    if(not rospy.is_shutdown()):
        rospy.loginfo("turning left" + str(rospy.get_time()))
        pub.publish()

#publishes a move forward topic which will turn the rover right
def movement_turnRight():
    pub = rospy.Publisher('movement/turnRight', Empty, queue_size=10)
    if(not rospy.is_shutdown()):
        rospy.loginfo("turning right" + str(rospy.get_time()))
        pub.publish()
