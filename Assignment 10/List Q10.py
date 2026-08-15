#Q10. Write a program to remove all occurrences of a given element in the list.

li = [5, 10, 5, 15, 20, 25]

num = int(input("Enter Number="))
new = []

for i in li:
    if i == num:      #[i] -> can't take it because i is already element, if (i==5): then [i] = [5]  <- list        continue
        continue
    else:
        new = new + [i]

print("List:", new)