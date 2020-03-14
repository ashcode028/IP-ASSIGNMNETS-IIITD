# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 13:40:23 2019

@author: ashita
"""
def reverse(s):
    return s[::-1]
def get_every_fourth(s):
    x=reverse(s)
    s=x.strip()
    y=s[::4]
    return reverse(y)
def get_every_kth(s,k,i):
    x=reverse(s)
    s=x.strip()
    l=len(s)
    z=(l-i)-1
    y=s[z::k]
    return reverse(y)
def decode_string(s):
    x=reverse(s)
    start=x.index('_')
    substr=x[start+1:]
    end=substr.index('_')
    inside=substr[:end]
    f=reverse(inside)
    return f
    
  
    