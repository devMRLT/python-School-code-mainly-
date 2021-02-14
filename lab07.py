# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 09:54:02 2018

@author: narmo
"""
counterGreater = 0
counterLesser = 0
#insertion Sort
def insertionSort(list1):
    for j in range(1, len(list1)):
        key = list1[j]
        i = j-1
        
        while i >= 0 and list1[i] > key:
            list1[i + 1] = list1[i]
            i = i - 1
        list1[i + 1] = key
    return list1
#Binary Search
def binarySearch(list1, low, high, x):
    global counterGreater
    global counterLesser
    #check the base case
    if high >= low:
        mid = int((low + high)/2)
        #check if it's within the middle of the list1
        if list1[mid] == x:
            return mid
        #if smaller than mid (left side of the list1)
        elif list1[mid] > x:
            counterLesser += 1
            return binarySearch(list1, low, mid-1, x)
        #Check if bigger than (right side of list1)
        else:
            counterGreater += 1
            return binarySearch(list1, mid+1, high, x)
    else:
        #return -1
        return -1
    return counterGreater
    return counterLesser
#inital list1
list1 = [int (l1) for l1 in input("Please enter a list1 use spaces!").split()]
print(list1)
insertionSort(list1)
print(list1)
x =  int (input("Please enter the value you would like to search for :"))
Outcome = binarySearch(list1, 0, len(list1)-1, x)

if Outcome != -1:
    print("X is within the list1")
    print("Number of > :", counterGreater, "\nNumber of < :", counterLesser)
else:
    print("X not found within the list1")