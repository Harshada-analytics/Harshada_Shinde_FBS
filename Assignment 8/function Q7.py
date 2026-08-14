#7. Write a program to find sum of digits of a number.

def number(num):
    total = 0

    while(num > 0):
        digit = num % 10 
        total = total + digit
        num = num // 10

    return total
    
num = int(input("Enter Number:"))
res = number(num)

print("Total:", res)

