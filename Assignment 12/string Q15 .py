#Q.15  15. Python Program to find larger string without using built-in functions.

string1 = input("Enter String1: ")
string2 = input("Enter String2: ")

count1 = 0
count2 = 0

for i in string1:
    count1 += 1

for i in string2:
    count2 += 1

if count1 > count2:
    print("Larger String:", string1)

elif count2 > count1:
    print("Larger String:", string2)

else:
    print("Both strings are same length")