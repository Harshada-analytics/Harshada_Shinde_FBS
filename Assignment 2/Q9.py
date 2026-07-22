#Q9. Write a program to swap two numbers without using third variable.

num1 = int(input("First Number : "))
num2 = int(input("secnond Number :"))

num1 = num1 + num2
num2 = num1 - num2 
num1 = num1 - num2

print("After swapping")
print("First numbers :", num1)
print("Second numbers :",num2)