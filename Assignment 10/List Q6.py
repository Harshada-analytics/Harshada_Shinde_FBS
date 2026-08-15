#6. Write a program to remove duplicates from the list.
li = [10, 20, 30, 20, 40]
new = []

for i in li:
    found = False

    for j in new :
        if i == j:
            found = True
            break

    if found == False:
        new = new + [i]
        
print("final :", new)
