#Q6.Python program to find union of two lists. (combine the elements of both lists and keep only unique elements # remove duplicates)

li1 = [1, 2, 3, 4, 5 ]
li2 = [2, 4, 5, 6, 7 ]

li1.extend(li2)
print("Merge_list:", li1)

union = []

for i in li1 :
    if i not in union:
        union.append(i)

print("Union List: ",union)


# extend()       → merge both lists
# for            → check every element
# if             → check whether already present
# not in         → avoid duplicates
# append()       → add unique element