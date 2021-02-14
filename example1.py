# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 15:30:02 2018

@author: narmo
"""

pi = 0
accuracy = 100000

for i in range(0, accuracy):
    pi += ((4.0 * (-1)**i) / (2*i + 1))

    print(pi)