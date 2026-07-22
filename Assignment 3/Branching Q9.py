#Q9. input 5 subject Marks from user and display grade. (eg.:first class, second class..) 

sub_1 = int(input("English :"))
sub_2 = int(input("Math :"))
sub_3 = int(input("History :"))
sub_4 = int(input("Geography :"))
sub_5 = int(input("Art :"))

total = sub_1 + sub_2 + sub_3 + sub_4 + sub_5 
Percentage = (total/500)*100
total_marks = Percentage

if(Percentage >= 90):
    print("Total Marks : ",Percentage)
    print("Grade : A+")

elif(Percentage >= 80):
    print("Total Marks : ",Percentage)
    print("Grade : A")

elif(Percentage>= 60):
    print("Total Marks : ",Percentage)
    print("Grade : B")

elif(Percentage >= 35):
    print("Total Marks : ",Percentage)
    print("Grade : C")

else:
    print("Fail")