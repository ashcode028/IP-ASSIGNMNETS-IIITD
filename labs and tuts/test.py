# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 14:52:53 2019

@author: ashita
"""

from a6 import *
from introcs import *
from labwrk import *
"""ques1"""
p1=Point(0,0)
l1=Line(1,1,-6)
findMirrorPoint(p1,l1)
assert_equals((p1.x,p1.y),(6.0,6.0))
print("done")

p1=Point(2,3)
l1=Line(1,1,-4)
findMirrorPoint(p1,l1)
assert_equals((p1.x,p1.y),(1.0,2.0))
print("done")



"""ques2"""
p1=Point(1,2)
p2=Point(1,1)
l1=Line(1,0,-1)
l2=Line(1,2,-1)
assert_equals(True,checkSides(p1,p2,l1,l2))
print("done1")

p1=Point(2,3)
p2=Point(4,2)
l1=Line(0,1,0)
l2=Line(3,-4,-7)
assert_equals(False,checkSides(p1,p2,l1,l2))
print("done1")  

"""ques3"""

c1=Circle(2,3,3)
c2=Circle(1,-1,4)
assert_equals(True,checkIntersection(c1,c2))
print("done2")

c1=Circle(2,3,3)
c2=Circle(2,3,4)
assert_equals(False,checkIntersection(c1,c2))
print("done2")
