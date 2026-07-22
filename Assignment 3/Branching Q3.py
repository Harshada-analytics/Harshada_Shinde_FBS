#Q3. Write a program to input angles of triangle and check whether it is valid or not.

angle1 = int(input("Enter angle 1 :"))
angle2 = int(input("Enter angle 2 :"))
angle3 = int(input("Enter angle 3 :"))

Total = (angle1 + angle2 + angle3)

if(Total == 180):
    print("Valid")
else:
    print("invalid")