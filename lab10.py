# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 10:35:36 2018

@author: narmo
"""
#initiate the class queue
class Queue:
    def __init__(self):
        self.items = []
        
    #check if the queue is empty
    def isEmpty(self):
        return self.items == []
    #add item to the back of the queue
    def enqueue(self,item):
        self.items.insert(0, item)
        
    #empty the queue
    def dequeue(self):
        return self.items.pop()
    
    def front(self):
        return self.item()
    
    def __str__(self):
        pass
    
q = Queue()
q.enqueue(4)
q.enqueue('dog')
q.enqueue(True)
print(q.size())
