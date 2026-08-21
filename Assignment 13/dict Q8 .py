#Q.8 Python Program to Count the Frequency of Words Appearing in a String Using
#a Dictionary.

text = "apple banana apple mango banana apple"

words = text.split()

frequency = {}      #empty dictionary

for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

print(frequency)