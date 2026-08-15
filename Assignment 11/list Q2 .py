#Q2. Python program to merge two list and sort it.

def merge_sort(li, li2):

   li.extend(li2)
   print("Merge :", li)
   li.sort()

   return li

li = [10, 20, 30, 40, 50]
li2 = [100, 90, 80, 70, 60]

result = merge_sort(li, li2)
print("After Sort :", li)

