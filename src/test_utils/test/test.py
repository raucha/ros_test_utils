#!/usr/bin/python
# -*- coding: utf-8 -*-
# license removed for brevity

# print("hellow world")
# exit(10)

from re import M
import time
import rospy
import argparse



PKG='test_foo'
# import roslib; roslib.load_manifest(PKG)  # This line is not needed with Catkin.

import sys
import unittest
from sensor_msgs.msg import LaserScan

## A sample python unit test
class TestBareBones(unittest.TestCase):

    def __init__(self):
        ## 確認のデータを生成
        self.got_msg = False

        ## subscribe開始
        rospy.Subscriber("scan", LaserScan,self.cb_scan)

        ## subscribe待ち
        i = 20
        while self.got_msg == False and i > 0:
            time.sleep(0.25)
            i -= 1
    
    def cb_scan(self, msg):
        self.got_msg = True
        self.msg = msg
        
    def test_subscribe(self):
        self.assertTrue(self.got_msg)
        # self.assertEquals(1, 1, "1!=1")

    def test_frame_id(self):
        self.assertEquals(1, 1, "1!=1")

if __name__ == '__main__':
    rospy.init_node('test', anonymous=True)
    while(rospy.rostime.get_time() == 0.0):
        print('Waiting for initial time publication')
        time.sleep(0.1)
    # start_time = rospy.rostime.get_time()
    # target_time = 2.0
    # while (rospy.rostime.get_time() - start_time) < target_time:
    #     print('Waiting for end time {} (current: {})'.format(target_time,(rospy.rostime.get_time() - start_time)))
    #     time.sleep(0.1)
    import rostest
    rostest.unitrun(PKG, 'test_bare_bones', TestBareBones)
