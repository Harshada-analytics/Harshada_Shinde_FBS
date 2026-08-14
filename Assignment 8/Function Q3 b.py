# Write a program to find sum of following series using functions :
#b. 1!+ 2! + 3! + 4!+..... + n!

def series(num):
    factorial = 1
    total_sum = 0

    for i in range(1, num+1):
        factorial = factorial * i
        total_sum = total_sum + factorial 

    return total_sum

num = int(input("Enter Number :"))
res = series(num)

print("Total = ", res)

    