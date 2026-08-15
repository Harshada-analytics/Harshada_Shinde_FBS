#Q4 Write a program to reverse the list.


li =  [5, 10, 15, 20, 25, 30]

rev = []
for ind in range(5, -1, -1):
    rev = rev + [li[ind]]

print(rev)