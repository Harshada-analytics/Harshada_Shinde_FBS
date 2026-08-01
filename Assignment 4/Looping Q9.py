#Q9. WAP to print all numbers in range, divisible by given number.

num1 = int(input("Enter for range:"))
num2 = int(input("Enter divisor NO:"))

for i in range(1, num1 + 1):
    if(i % num2 == 0 ):
        print(i) 