#Q12. Write a program to check if given number is Armstrong number or not.
#(Hint : 153 = 1*1*1 + 5*5*5 + 3*3*3 , 1634 = 1*1*1*1 + 6*6*6*6 + 3*3*3*3 +
#4*4*4*4)

num = int(input("Enter Number: "))

original = num
digits = len(str(num))
total = 0

while num > 0:
    digit = num % 10
    
    total = total + (digit ** digits)

    num = num // 10

if total == original:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")