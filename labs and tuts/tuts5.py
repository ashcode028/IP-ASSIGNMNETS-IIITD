# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 13:28:45 2019

@author: ashita
"""

"""ques1()"""
a= int(input('a'))
b= int(input('b'))
c= int(input('c'))
def no_teen_sum(a,b,c):
    x=fix_teen(a)
    y=fix_teen(b)
    z=fix_teen(c)
    print (x+y+z)

def fix_teen(n):
    if(n==13 or n==14 or n==17 or n==18 or n==19):
     return 0
    else:
     return n
no_teen_sum(a,b,c)




"""ques3()"""
x= int(input('marks'))
def marks(a):
        if(a>90 and a<=100):
         return "A"
        elif(a>75 and a<=90):
         return "B"
        elif(a>60 and a<=75):
         return "C"
        elif(a>45 and a<=60):
         return "D"
        else:
         return "F"
t=marks(x)
print (t)


"""ques4()"""
y=input('string')
k= int(input('k'))
def check(k):
    if(k%3==0 and k%5!=0 or k%3!=0 and k%5==0):
        return k
    else:
        return 0
z=check(k)
print(y+(y*z))



"""ques5()"""
p= int(input('p'))
q= int(input('q'))                    
def check_sign(i,j):
    if(i<0 and j<0 or i>0 and j>0):
        return "same sign"
    elif(i==0 or j==0):
        return "atleast one of them is zero"
    else:
        return "different sign"
h= check_sign(p,q)
print (h)    

