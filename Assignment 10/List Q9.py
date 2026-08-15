#Q9. Write a program of having n number of elements in the list and find out even
#and odd elements in that list and then create two separate lists which will have
#even elements and other will have odd elements.

li = [1, 2, 3, 4, 5, 6, 7, 8]
even = []
odd = []

for i in li:

    if (i % 2 == 0):
        even = even + [i]
    else:
        (i % 2 != 0)
        odd = odd + [i]

print("List =", li)
print("Even :",even)
print("Odd :", odd)