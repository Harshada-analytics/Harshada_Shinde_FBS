#Q9. Write a program to check if entered number is a palindrome or not.and

def palindrome(number) :
    temp = number
    rev = 0

    while (number > 0):
        digit = number % 10
        rev = rev * 10 + digit
        number = number // 10  

    if (temp == rev ):
        print("Number is Palindrome") 
    else:
        print("Not palindrome")

number = int(input("Enter Number:"))
res = palindrome(number)

