#c. 1^1 + 2^2 + 3^3+ ...... n^n

def series(num):
    
    total = 0

    for i in range(1, num+1):
        power = i ** i
        total = total + power

    return total

number = int(input("Enter Number:"))
res = series(number)
print("Total Sum =", res)
