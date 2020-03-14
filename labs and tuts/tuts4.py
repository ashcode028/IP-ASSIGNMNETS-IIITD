# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 09:12:07 2019

@author: ashita
"""

a=input('a')
b=input('b')
def anagram(a,b):
    a=sorted(a)
    b=sorted(b)
    return a==b
print(anagram(a,b))



s=input('enter string')
def findDirectory(s):
    x=s[::-1]
    y=x.find("/")
    k=x[:y]
    return k[::-1]
print(findDirectory(s))



def palindrome(s):
    x=s[::-1]
    if (s==x):
        return 'it is a palindrome'
    else:
        return 'it is not'
print(palindrome('ashita'))    