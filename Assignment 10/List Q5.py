#Q5.Accept a number from user and check if this element is present in the list or
#not. Also tell how many times it is present in the list.

li = [10, 20, 10, 30, 10, 40]
num = int(input("Enter Number:"))
count = 0
for i in li:
    if i == num :
        count += 1
if count == 0:
    print("Element is not present.")
else:
   print("Element is present.")
   print("How many times present:",count)


#1. Take a number from the user.
#2. Start count = 0.
#3. Visit every list element using a loop.
#4. If element == user's number, increase count.
#5. If count is 0 → element is not present.
#6. Otherwise → element is present and count tells how many times.