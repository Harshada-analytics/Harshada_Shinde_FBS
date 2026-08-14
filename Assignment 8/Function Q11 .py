#Q11. WAP to check given number is Armstrong number or not. For each task create seaprate function.

def armstrong(number):
    count = len(str(number))
    temp = number
    total = 0

    while number > 0:
        digit = number % 10
        total = total + digit ** count
        number = number // 10

    if temp == total:
        print("Armstrong Number")
    else:
        print("Not Armstrong Number")


num = int(input("Enter Number:"))
armstrong(num)

