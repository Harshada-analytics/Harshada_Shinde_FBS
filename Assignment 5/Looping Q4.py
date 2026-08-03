#Q4 WAP to print Armstrong number within a given range.

start = int(input("Enter start Number:"))
end = int(input("Enter end number:"))

num = start

while num <= end:

    temp = num
    count = 0

    while temp > 0:
        count += 1
        temp = temp // 10

    temp = num
    total = 0

    while temp > 0:
        digit = temp % 10
        total = total + (digit ** count)
        temp = temp // 10

    if total == num:
        print(num)

    num += 1