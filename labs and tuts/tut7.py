# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 08:53:32 2019

@author: ashita
"""
"""
ques1
"""
s=input("enter a string")
def noOFVowel(s):
    vowel=[0,0,0,0,0]
    d= {'a':0,'e':1,'i':2,'o':3,'u':4}
    for i in range(len(str(s))):
        if( s[i] in d): 
           vowel[d[s[i]]]+=1
    print(vowel)
noOFVowel(s)    
"""ques2
"""
def oddeven(l,n):
    even=0
    odd=0
    for i in range(n):
        if (i%2==0):
            even+=l[i]
        else:
            odd+=l[i]
    return even-odd    
print(oddeven([4,5,6,7],4))
"""
ques3
"""
n=int(input("enter the number"))
for i in range(n):
    print(i+1)
for i in range(n):
    print('*'*(i+1))



no=1
for i in range(n):
    print('\r')
    for j in range(i+1):
        print (no,end='')
        no+=1



k=2*n-2
for i in range(n):
    print('\r')
    for j in range(k):
        print(end=' ')
    k=k-1
    for j in range(i+1):
        print('*',end=' ')



k=2*n-2       
for i in range(n):
    print('\r')
    for j in range(k):
        print(end=' ')
    k=k-2
    for j in range(i+1):
        print('*',end=' ')
    
    