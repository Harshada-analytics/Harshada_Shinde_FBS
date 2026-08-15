#Q3. Write a program to find the second largest element in list.


li = [45, 12, 78, 23, 9, 56]
max1 = 0
max2 = 0

for i in li:
    if(i > max1):
        max2 = max1             #When a new largest comes, the old largest becomes second largest.
        max1 = i                #max1 value contains at max2 and i's value contains max1.

    elif (i > max2):
        max2 = i 

print("The Max1 no.:",max1)
print("The Max2 no.:",max2)