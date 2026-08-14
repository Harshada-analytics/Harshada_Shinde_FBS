#Q2. WAP to calculate area of circle. 

import math 

def circle(radius):
   
   area = math.pi * radius * radius
   return area

radius = float(input("Enter Radius : "))

res = circle(radius)

print("Area Of Circle: ",res)