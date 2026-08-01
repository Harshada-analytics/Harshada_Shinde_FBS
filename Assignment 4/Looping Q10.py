#Q 10 WAP a program to check given number is Perfect Number.

num = int(input("Enter Number:"))
divisor_sum = 0
for i in range(1, num):
    if(num % i == 0 ):
        divisor_sum += i

if (divisor_sum == num):
    print("Perfect Number")
else:
     print("Not Perfect")

