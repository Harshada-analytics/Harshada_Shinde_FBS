#Q.1 Write a python program to find elements in a given set that are not in another set.

set1 = {"1", "2", "3", "4"}
set2= {"1", "2", "5", "6"}

total = set1 - set2   #“give me elements that are in set1 but not in set2.”

print(total)