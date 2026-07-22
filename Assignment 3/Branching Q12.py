#Q12. Write a program to check if a given 3 digit number is palindrome or not.

num = int(input("Enter digits :"))
original = num 

rev = 0
while(num > 0):

    digit = num % 10
    num = num // 10
    rev = rev * 10 + digit
    print(digit)

if(original == rev):
    print("NUmber  is palindrome")
else:
    print("Number is not palindrome")