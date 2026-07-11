#Q7. Program to find Quadratic equation. 

#input
import math 

a = float(input("Enter value of a :"))
b= float(input("Enter value of b :")) 
c = float(input("Enter value of C :"))

#perform operation
d= (a * b) - (4 * a * c)

x1 = (-b + math.sqrt(d)) / (2 * a)
x2 = (-b - math.sqrt(d)) / (2 * a)

#Display output
print("Root 1 =", x1)
print("Root 2 =", x2) 