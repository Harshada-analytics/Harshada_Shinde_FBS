#Q7.Python program to find the intersection of two lists.

li1 = [1, 2, 3, 4, 5, 7]
li2 = [2, 4, 6, 7, 8, 9,]

intersection = []

for i in li1:
    if i in li2:
        intersection.append(i)

print("Intersection:", intersection)



#Union:
#merge → remove duplicates

#Intersection:
#take one list → check whether element is present in other list