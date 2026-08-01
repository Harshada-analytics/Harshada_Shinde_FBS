#Q11 WAP to check if given number Strong Number.

num = int(input("Enter Number:"))

original = num 
total = 0

while num > 0:
    digit = num % 10

    fact = 1     # Find factorial of the digit
    for i in range(1, digit + 1):
        fact = fact * i

    total = total + fact

    num = num // 10

if(total == original):
    print("Strong Number")
else:
    print("Non strong NUmber")
