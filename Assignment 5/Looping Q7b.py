# Q7b. N + N^2 + N^3+N^4 .....+N^N (here ^ means exponent)

n = int(input("Enter Number: "))

sum = 0

for i in range(1, n + 1):

    power = 1

    for j in range(1, i + 1):
        power = power * n

    sum = sum + power

print("Sum =", sum)