"""
Created on Thu Nov 29 09:31:40 2018
@author: narmo
"""
import math
#parent class
class Shape():
   def  __init__(self, width, height, radius):
        self.width = 13
        self.height = 15
        self.radius = 16
        self.area1 = 0
        self.perimeter1 = 0 
        self.area2 = 0
        self.perimeter2 = 0 
        
#rectangle child class
class rectangle(Shape):
    def getArea(self):
       return self.width * self.height
   
    def getPerimiter(self):
       return self.width*2 + self.height*2

#cicle child class
class circle(Shape):
    def getArea(self):
       return math.pi * self.radius^2
   
    def getPerimiter(self):
       return 2*math.pi * self.radius

