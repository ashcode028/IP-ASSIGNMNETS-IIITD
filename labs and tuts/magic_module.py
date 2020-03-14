# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 13:52:13 2019

@author: ashita
"""

def find_magic_num(x,y,z):
    """
    to find magic number"""
    magicno = (((x*x)+y)%z)**5
    return magicno
print(find_magic_num(1,3,5))