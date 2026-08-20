#Q8. Pyhton Program to Remove the character of Odd Index Values in a string.

String = "HINDUSTAN"

new_str = "" 

for i in range(len(String)):

    if (i % 2 == 0):
       new_str += String[i] 

print("New :", new_str)
        