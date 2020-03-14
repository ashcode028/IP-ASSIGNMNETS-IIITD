# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 14:34:07 2019

@author: ashita
"""
from string_functions_2019028 import *

print(get_every_fourth ("hello world"))
print(get_every_fourth (" encyclopedia "))
print(get_every_fourth ("    python  "))



print(get_every_kth ("document",2,5))
print(get_every_kth ("  Hi There  ",2,7))
print(get_every_kth ("  Oh My God!!   ",3,9))
print(get_every_kth ("   introduction    ",3,8))



print(decode_string ("abc_dEf_xy45_12z_mNOp"))
print(decode_string ("Hi There_Hello World_123 abc"))
print(decode_string ("aBc_123_care_love"))


from a6 import *
import math
from labwrk import *


p=Point(1,0)
i=Line(-1,1,0)
findMirrorPoint(p,i)
print(p.x,p.y)

p1=Point(-2,0)
p2=Point(1,1)
i1=Line(-1,1,0)
i2=Line(-2,1,-1)
print(checkSides(p1,p2,i1,i2))

c1=Circle(-2,0,3)
c2=Circle(4,0,3)
print(checkIntersection(c1,c2))

