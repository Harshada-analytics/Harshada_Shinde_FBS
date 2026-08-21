#Q.5 Python Program to Sum All the Items in a Dictionary

dictionary = {

    "A": "2",
    "B": "3",
    "C": "4"
}

total = 0

for value in dictionary.values():   #dictionary.values() -> gives the values
    total = total + int(value)

print("Sum :", total) 