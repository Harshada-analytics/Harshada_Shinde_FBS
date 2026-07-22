#Q4. Write a progrm to input all sides of triangle and check whether it is valid or not.

side1 = int(input("Enter side 1 :"))
side2 = int(input("Enter side 2 :"))
side3 = int(input("Enter side 3 :"))

if(side1 + side2 > side3):
    print("Valid")
else:
    print("Invalid")