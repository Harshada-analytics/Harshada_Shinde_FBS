#Q.11 Write a program to print all numbers which are divisible by m and n in the list.

li = [10, 12, 15, 20, 24, 30, 36]

m = int(input("Enter m:"))
n = int(input("Enter n:"))

new = []

for i in li:

    if i % m== 0 and i % n == 0:
      new = new + [i]

print("li:",new)