#6. Python Program to Take in a String and Replace Every Blank Space
#with Hyphen.

string = "I am a good Programmer"

new_string = ""
size = len(string)

for i in string :

    if i == " " :
      new_string = new_string + "-"
    else:
        new_string += i

print ("New =", new_string)

