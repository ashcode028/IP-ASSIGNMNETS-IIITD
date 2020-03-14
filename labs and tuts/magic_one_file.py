# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 13:59:50 2019

@author: ashita
"""
def find_magic_no(x,y,z):
     """
     to find magic number"""
     magicno = (((x*x)+y)%z)**5
     return magicno


i=int(input())
j=int(input())
k=int(input())
print(find_magic_no(i,j,k))
