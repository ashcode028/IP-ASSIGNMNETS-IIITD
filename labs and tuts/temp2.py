# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 21:47:27 2019

@author: ashita
"""
from fractions import Fraction as frac
if __name__=="__main__":
    arr=list(map(float,input().split()))
    d=sum(arr)
    s=frac(arr[0]/d)
    f=frac(arr[1]/d)
    p=6
    t=0
    def prob(x,s,f):
        k=p-x
        return (s**x)*(f**k)
    for i in range(3,7):
        t+=prob(i,s,f)
        print(t)
    #print(round(t,3))
    