#Q.10  Take in two strings and Display the larger String without using built-in function

string1 = "Harshada"
string2 = "Tanisha"

count1 = 0
count2 = 0

for i in string1 :
    count1 += 1

for x in string2 :
    count2 += 1

if count1 > count2 :
    print("Larger String :", string1 )

elif count2 > count1 :
    print("larger String2 :", string2)

else :
    print("Both strings are same length") 

        