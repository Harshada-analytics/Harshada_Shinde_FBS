#Q.11 python program to replace every blank space with hyphen in a string.

string = "I Want to become a Data Analyst"

new = ""

for i in string :

    if i == " " :
        new = new + "-"
    else :
        new = new + i
        
print("New :",new)