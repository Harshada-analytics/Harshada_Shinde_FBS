# Q.12 Python Program to count a number of lowercase characters in a string.

string = "Data Analyst"

count = 0

for i in string :

    if i >= "a" and i <= "z" :
        count += 1

print("lower case:", count)

# Take character
#     ↓
# Is it between a and z?
#    ↓
# Yes → count + 1
# No  → skip