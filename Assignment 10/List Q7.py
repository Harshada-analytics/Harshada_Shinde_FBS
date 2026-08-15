#Q7. WAP to create a new list from from existing list which contains cube of each number of list.

li = [2, 3, 4, 5]
new = []

for i in li:
    new = new + [i * i * i]

print("New list:", new)   