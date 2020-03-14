# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 19:14:11 2019

@author: ashita
"""
from a6 import *
import math

def findMirrorPoint(p,i):
    k=-(2*(i.a*p.x+i.b*p.y+i.c))/(i.a**2+i.b**2)
    p.x=k*i.a+p.x
    p.y=k*i.b+p.y

def checkSides(p1,p2,i1,i2):
    findMirrorPoint(p1,i1)
    f=p1.x*i2.a+p1.y*i2.b+i2.c
    j=p2.x*i2.a+p2.y*i2.b+i2.c
    if((f>0 and j>0) or (f<0 and j<0)):
        return True
    else:
        return False
def checkIntersection(c1,c2):
    d=math.sqrt((c1.centre_x-c2.centre_x)**2 +(c1.centre_y-c2.centre_y)**2)
    r=c1.radius+c2.radius    
    if(d<r and d!=0):
        return True
    elif(d==0 and d==r):
        return False
    else:
        return False
     
    
    