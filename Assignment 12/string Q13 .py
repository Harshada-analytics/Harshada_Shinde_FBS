#Q.13 python program to count number of digits and letters in a string.

string = "harsha1 varsha2 Tanisha3"

count1 = 0
count2 = 0 

for i in string :

    if (i >= "a" and i <= "z") or (i >= "A" and i <= "Z"):
        count1 += 1
        
    elif i >= "0" and i <= "9" : 
       count2 += 1

print("Characters :",count1)
print("Digits :", count2)
