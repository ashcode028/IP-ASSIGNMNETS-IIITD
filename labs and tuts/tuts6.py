# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 11:14:28 2019

@author: ashita
"""
#ques1
def change_date(date,year_fix):
    """ 
    returns new date, with year_fix numerically added to the original year.
    returns string of form "dd mm yyyy"
    date: a str of the form "mm dd yyyy"
    precondition: date is a string of only numbers and ' '.
    """
    new_year=year_fix+int(date[6:])
    return date[3:5]+"-"+date[:2]+"-"+str(new_year)
#ques2    
from m1 import *
score=int(input("enter score"))
player=input('enter player name')
coins=int(input('enter no of coins'))
obj=game(score,player,coins)
if (obj.coins>100):
    score+=1000
else:
    score-=1500
    if(obj.score<0):
        obj.score=0
        