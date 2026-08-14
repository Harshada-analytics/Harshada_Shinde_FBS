#Q5. Sum of all prime numbers between 1 to n.

def series(num):
    total = 0

    for i in range(2, num+1):
        count = 0

        for j in range(1, i + 1):
            if (i % j == 0 ):
                count = count + 1

        if count == 2:
            total = total + i

    return total

numbers = int(input("Enter Number:"))
res = series(numbers)

print("Total_sum :", res)