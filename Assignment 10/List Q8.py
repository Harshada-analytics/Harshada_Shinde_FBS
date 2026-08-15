#Q8. WAP to create a duplicate of an existing list. It should not point to same list.

li = [10, 20, 30]
new = []

for i in li:
    new = new + [i]

print("Old:", li)
print("New:", new)
