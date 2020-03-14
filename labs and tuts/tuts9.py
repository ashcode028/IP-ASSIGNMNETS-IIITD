# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 13:36:11 2019

@author: ashita
"""


class date():
    def __init__(self,month,day,year):
        self.month=month
        self.day=day
        self.year=year
    
    def getmonth(self):
        return self.month
    def setmonth(self,m):
        self.month=m
    def getday(self):
        return self.day
    def setmonth(self,d):
        self.day=d
    def getyear(self):
        return self.year
    def setyear(self,y):
        self.year=y
    
    
class movie():


class myobj:
    def __init__(self,k=8):
        self.x = 8
        print(self.x)
    def __str__(self):
        return str(self.x)
    def scale(self,a,b):
        a.x = a.x * b
        print(a.x)

s = myobj()
t = myobj(4)
print(s)
s.scale(t,2)
print(t)









