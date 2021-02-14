# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 09:37:37 2018

@author: narmo
"""
from random import shuffle#import for shuffle
def insertionSort(arr):
    count = 0
    for j in range(1, len(arr)):
        key = arr[j]
        i = j-1
        
        while i >= 0 and arr[i] > key:
            count = count + 1#count the  operation iteration
            arr[i + 1] = arr[i]
            i = i - 1
           
        arr[i + 1] = key
    print("These are the number of iterations through", count)
    print(arr)
print("Welcome to the insertion sort lab!!!")
#inital list
arr = [int (set2_var2) for set2_var2 in input().split()]
#shuffle list into random order
shuffle(arr)
print(arr)
#sort list in assending order
insertionSort(arr)
#output the final list

