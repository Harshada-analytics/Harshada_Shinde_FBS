#Q10.  Write a program to print list after removing numbers.

li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new = []

for i in li:
     if(i % 2 != 0):
        new = new + [i]

print("New:", new)


#using Function :
# If you want to put this same program inside a function, you can do it like this:

def remove_even(li):
    new = []


    for i in li:
        if i % 2 != 0:
            new = new + [i]

    return new

li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

res = remove_even(li)
print("New:", res)


# another, without parameter
def odd():

    li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    new = []

    for i in li:
        if i % 2 != 0:
            new = new + [i]

    return new


res = odd()

print("New:", res)