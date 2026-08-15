#q5. Python program to sort a list accordiing to the length of the elements withiin the list.

li = ["cat", "elephant", "dog", "tiger"]

for i in range(len(li)):
    for j in range(0, len(li) - i -1):

        if len(li[j]) > len(li[j+1]):      #if(li[j] > li[j+1]):
           li[j], li[j+1] = li[j+1], li[j]

print(li)