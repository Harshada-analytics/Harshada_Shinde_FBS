#1. Write a program to find the area and perimeter of following figure (Accept the
#length, breadth and radius from user:

import math

length = float(input("Enter length:"))
breadth = float(input("Enter breadth:"))
radius = float(input("Enter radius:"))

area_rectangle = length*breadth

area_semicircle = (math.pi * radius * radius)/2

area = area_rectangle + area_semicircle

perimeter = (2 * length) + breadth + (math.pi * radius)

print("Area of the figure :", area)
print("Perimeter of the figure :", perimeter)