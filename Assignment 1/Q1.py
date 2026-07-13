#Q1. Write a program to calculate percentage of student based on marks of any 5 subjects. 

#Take input
sub1 = float(input("Enter sub1 Marks :"))
sub2 = float(input("Enter sub2 Marks :"))
sub3 = float(input("Enter sub3 Marks :"))
sub4 = float(input("Enter sub4 Marks :"))
sub5 = float(input("Enter sub5 Marks :"))

#Perform operation
#percentage = obtained marks/Total Marks*100

obtained_marks= sub1 +sub2 + sub3 +sub4 +sub5
Total = obtained_marks/500*100

#Display result
print("Total Marks:",obtained_marks)
print("percentage :",Total,"%")
