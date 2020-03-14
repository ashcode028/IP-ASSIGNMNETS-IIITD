# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 21:47:27 2019

@author: ashita
"""

from introcs import *
from tuts6 import *
#first test case
assert_equals(change_date("12 05 2000",18),"05-12-2018")
#second test case
assert_equals(change_date("11 01 1999",2),"01-11-2001")
#third test case
assert_equals(change_date("01 11 2010",-3),"11-01-2007")
print("done")