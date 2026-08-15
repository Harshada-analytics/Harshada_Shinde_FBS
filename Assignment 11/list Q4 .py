#Q4. Python program to find the second largest Number in a list using bubble sort.

li = [1, 2, 7, 4, 5, 8, 3]

for i in range(len(li)):
    for j in range(0, len(li) - i-1):

        if (li[j] > li[j+1]):
            li[j], li[j+1] = li[j+1], li[j]

second_largest = li[len(li) - 2]

print("Second Largets : ", second_largest)