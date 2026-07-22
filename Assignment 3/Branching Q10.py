#Q10.Write a program to check if a person eligible to marry or not (male age >= 21 and female age >= 18).

gender = (input("Enter gender(M/F) : ")).upper()
age = int (input("Enter age :"))

if(gender == "F" ):
    if(age >= 18):
        print("The girl is Eligible to Marriage")
    else:
        print("Not Eligible to Marriage")

elif(gender == "M"):
    if(age >= 21):
        print("The boy is Eligible to Marriage")
    else:
        print("Not Eligible to Marriage")
else:
    print("Invalid gender")