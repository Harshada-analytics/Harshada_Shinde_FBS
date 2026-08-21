#Q. 6. Python Program to Multiply All the Items in a Dictionary

dictionary = {

    "A" : "2",
    "B" : "3",
    "C" : "4"
}

total = 1        #not 0 -> because 0*2*3*4 = 0

for value in dictionary.values():
    total = total * int(value)

print("Multiply :", total)