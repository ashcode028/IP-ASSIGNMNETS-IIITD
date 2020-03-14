# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 19:00:45 2019

@author: ashita
"""

def lastOne(y,x): 
    x ^= y  
    y ^= x 
    x ^= y 
    return x 
def finalOne(x,y): 
    x,y=y,x 
    return lastOne(y,x) 
def anotherOne(x,y): 
    x=x+y
    y=x-y
    x=x-y 
    return finalOne(x,y) 
def one(x,y): 
    t=x 
    x=y
    y=t 
    return anotherOne(y,x) 
x=6
y=9 
print(one(x,y)) 



def tripleTrouble(x,y,z): 
    y+=x 
    z=y//2 
    x=int(False!=z>=x+int(14.9) and y*7<=14) 
a="IIIT" 
b="Delhi" 
x=len(a+b) 
y=x%7 
z=14-2**4>>2 
tripleTrouble(y,x,z) 

  


def secretMsg(w):
    a=w.index('(')
    b=w.index(')')
    c=w[b:-1]
    d=len(c)-1
    e=w[a+1:b]
    print('#'+str(d)+'"'+ e[::-1] +'"'+w[:a] +'#')
secretMsg('how(you)doing?')   





x=int(input('x'))
A=input('A')
def checkIt(x,A):
    l=len(A)
    m=l-1
    if(l%x!=0):
        print(l-(l%x))
    else:
        print(m-(m%x))
    if(l>x or (l%2==0)):
        return 'True'
    else:
        return 'False'
Z=checkIt(x,A)    
print(Z)





import re
def playString(A,B):
        a=A.lower()
        print('a' and 'e' and 'i' and 'o' and 'u' in A)
        print(B in A)
        z=len(re.findall('[bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ]',B))
        return z
k=playString('whatISeutopia','eutopia')    
print (k)
    
    