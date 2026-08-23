#Q.9 Write a Python program to find all the unique combinations of 3numbers 
# from a given list of numbers, adding up to a target number.

def combination(numbers, target):

    for i in numbers:            #Because the question says “combinations of 3 numbers.”
        for j in numbers:
            for k in numbers:

                if i < j and j < k:
                    if i + j + k == target:
                        print(i, j, k)

numbers = {1, 2, 3, 4, 5, 6}

target = int(input("Enter target: "))

combination(numbers, target)