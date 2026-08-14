#8. Write a program find reverse of a number.

def reverse(num):
    rev = 0

    while num > 0:
        digit = num % 10
        rev = rev * 10 + digit 
        num = num // 10 

    return rev

number = int(input("enter Number:"))
res = reverse(number)

print("Reverse No.:", res)