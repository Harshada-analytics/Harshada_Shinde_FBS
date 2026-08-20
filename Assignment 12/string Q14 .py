#Q. 14. Python Program to count the occurrences of each word in a string.

string = "I am a good and I am happy"

words = string.split()
new = []

for word in words:

    if word not in new:
        count = words.count(word)
        print(word, ":", count)
        new = new + [word]
        