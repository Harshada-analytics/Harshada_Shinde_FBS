#Q1. Python Program to Replace all occurances of 'a' with $ in a string.

string = input("Enter Input : ")
new = " "
for i in string:

    if (i == "a"):
        new += "$"
    else :
        new += i 

print(new)
        

