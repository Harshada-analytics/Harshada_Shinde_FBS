#Q1. Python program to put even and odd elements of a list into two differnet lists.

li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even = []
odd = []

print("List :", li)
for i in li:
    if (i % 2 == 0):
        even = even +  [i]
    else :
        odd = odd + [i]
    
print("even :", even)
print("Odd :", odd)
