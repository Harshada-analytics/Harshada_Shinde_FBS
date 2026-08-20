#Q5. Python Program to Count the Number of Vowels in a String

def vowels(string):

    count = 0

    for i in range(len(string)):

        if (string[i] == "a"):
         count += 1

        elif (string[i] == "e"):
         count += 1

        elif (string[i] == "i"):
         count += 1

        elif (string[i] == "o"):
         count += 1

        elif (string[i] == "u"):
         count += 1

    return count

string = input("Enter String: ")
count = vowels(string)

print("Vowels Count =", count)
