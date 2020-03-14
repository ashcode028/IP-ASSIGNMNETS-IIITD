# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 08:44:14 2019

@author: ashita
"""

def fibonacci(n):
    if(n==1):
        return 0
    elif(n==2):
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
#it is not efficient code

def linear_search(arr,low,high,x):
    if(low>high):
        return -1
    if(arr[high]==x):
        return high
    else:
        return linear_search(arr,low,high-1,x)
        
def pascal_triangle(n):
    if(n==1):
        return[1]
      
    else:
        if(n==2):
            return([1,1])
        else:
                l=pascal_triangle(n-1)
                print(l)
                l1=[1]
                for i in range(len(l)-1):
                    l1.append(l[i]+l[i+1])
                l1.append(1)
                return(l1)
        
print(pascal_triangle(6))

def countPairs(s):
    if(len(s)<3):
        return 0
    elif(s[0]==s[2]):
        return 1 + countPairs(s[1:])
    return countPairs(s[1:])
print(countPairs("ashita"))
 

#####################################
# EXAMPLE:  Towers of Hanoi
#####################################

def printMove(fr, to):
    print('move from ' + str(fr) + ' to ' + str(to))

def Towers(n, fr, to, spare):
    if n == 1:
        printMove(fr, to)
    else:
        Towers(n-1, fr, spare, to)
        Towers(1, fr, to, spare)
        Towers(n-1, spare, to, fr)

print(Towers(4, 'P1', 'P2', 'P3'))

    