#Q.12. Write a program to create three lists of numbers, their squares and cubes.

li = [2, 4, 5, 6, 7]

square = []
cube = []

for i in li:
        square = square + [i * i]
        cube = cube + [i * i * i]

print("List:", li)
print("Square:", square)
print("Cube:",cube)