# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 20:37:13 2018

@author: narmo
"""
def max_number(list):
   max = list[0]
   for a in list:
       if a > max:
           max = a
   return max
print(max_number([7,8,9,0,10]))
    
