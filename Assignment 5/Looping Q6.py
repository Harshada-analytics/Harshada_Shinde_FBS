#Q6. Write a program to print first n prime numbers.

n = int(input("Enter how many prime numbers: "))

count = 0
num = 2

while count < n:

    sum = 0

    for i in range(1, num + 1):
        if num % i == 0:
            sum += 1

    if sum == 2:
        print(num)
        count += 1

    num += 1
