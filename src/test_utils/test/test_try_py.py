#!/usr/bin/python
# -*- coding: utf-8 -*-
# license removed for brevity

# print("hellow world")
# exit(10)


PKG='test_foo'
# import roslib; roslib.load_manifest(PKG)  # This line is not needed with Catkin.

import sys
import unittest

## A sample python unit test
class TestBareBones(unittest.TestCase):

    def test_one_equals_one(self):
        self.assertEquals(1, 1, "1!=1")
    def test_one_equals_one2(self):
        self.assertEquals(1, 2, "1!=1")

if __name__ == '__main__':
    import rosunit
    rosunit.unitrun(PKG, 'test_bare_bones', TestBareBones)
