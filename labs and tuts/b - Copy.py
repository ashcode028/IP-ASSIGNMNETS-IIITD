# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 22:14:21 2019

@author: ashita
"""
import a1 
def f(x): 
    print(id(x)) #line 4 
    x=8 
    print(id(x)) #line 5 
y=7 
print(id(y)) 
f(y) 
z=7 
print(id(y)==id(z)) #line 6 
print(id(f(7))==id(f(9))) #line 7 
print(id(f(7))==a1.f(7)) #line 8 


