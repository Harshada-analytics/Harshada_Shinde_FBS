#Q7d. S = a + a2 / 2 + a3 / 3 + ...... + a10 / 10

a = int(input("Enter Value of a: "))

sum = 0

for i in range(1, 11):

    power = 1

    for j in range(1, i + 1):
        power = power * a

    sum = sum + (power / i)

print("Sum =", sum)