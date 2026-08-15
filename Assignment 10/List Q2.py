#Q2. Write a program to find a maximum and minimum element in a list.

li = [45, 12, 78, 23, 9, 56]

max1 = li[0]
min1 = li[0]

for ind in range(1, len(li)):        #need index/position
    if(li[ind] > max1):
        max1 = li[ind]

    if(li[ind] < min1):
        min1 = li[ind] 

print('Maximum Element:', max1)
print('Minimum element:', min1)

#or
li = [45, 12, 78, 23, 9, 56]

max1 = li[0]
min1 = li[0]

for i in li:                  #need only values
    if i > max1:
        max1 = i

    if i < min1:
        min1 = i

print("Maximum:", max1)
print("Minimum:", min1)