#Q9. Write a program to create three lists of numbers, their squares and cubes.

li = [2, 3, 4, 5, 6]

square = []
cube = []

for i in li:

    square = square + [i ** 2]
    cube = cube + [i ** 3]

print("List:", li)
print("Square:", square)
print("Cube:", cube)

