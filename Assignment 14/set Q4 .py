#Q.4 Write a Python program that finds all pairs of elements in a list whose
#sum is equal to a given value.

num = int(input("Enter Number :"))
list = [2, 4, 5, 6, 7, 8, 9 ]

for i in list:
    for j in list:
      
      if i + j == num:

        print(i, j)