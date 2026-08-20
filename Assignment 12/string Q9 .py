#Q 9. pyhon program to calculate the Number of words and the Number of charactes present in a sting.

string = "I am a good programmer"

char_count= 0
words_count= 1             #why 1 ? - if there are 5 words, there are only 4 spaces.
                           #Therefore start: words_count = 1
for i in string:

    if i == " ":
        words_count += 1
    else:
      char_count += 1

print("Char_count ", char_count)
print("Word_count ", words_count)