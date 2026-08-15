#Q3. Python program to sort the list according to the second Element in sublist.

li  = [[1, 20], [2, 30], [3, 40], [4, 50]]

for i in range(len(li)):
    for j in range(i+1, len(li)):

        if (li[i][1] > li[j][1]):    
          
          temp = li[i]    #swapping
          li[i] = li[j]  
          li[j] = temp

print("Result :", li)
        