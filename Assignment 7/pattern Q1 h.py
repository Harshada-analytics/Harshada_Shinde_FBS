#Q h.

k = 9

for i in range(1, 6):

    for j in range(1, i + 1):
        print(j, end=" ")

    for j in range(1, k):
        print(" ", end=" ")

    for j in range(i, 0, -1):
        print(j, end=" ")

    k = k - 2

    print()