#Q5. Write a program to check whether the triangle is equilateral , isoscales or scalene triangle .

Angle1= int(input("Enter Angle 1 :"))
Angle2= int(input("Enter Angle 2 :"))
Angle3= int(input("Enter Angle 3 :"))

if(Angle1 == Angle2 == Angle3):
    print("Equilateal Triangle")   #All angles are same of triangle.

elif(Angle1 == Angle2 or Angle2 == Angle3 or Angle1==Angle3):
    print("Isosceles Triangle")      #Any 2 Angles are same.

elif(Angle1 != Angle2 != Angle3):   
    print("Scelen Triangle")          #Each angle is diifferent(40,30,60)
else:
    print("It is Invalid")