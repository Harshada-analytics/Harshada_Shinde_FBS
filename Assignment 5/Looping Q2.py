#Q2.Enter number of students from user. For those many students accept marks of 5
#subject marks from user and calculate percentage. Display all percentage and average percentage of student.


Students_Num = int(input("Enter Number of Students: "))
total_percentage = 0

for student in range(1, Students_Num + 1):
    total_marks = 0

    for subject in range(1, 6):
        marks = int(input("Enter Marks: "))
        total_marks += marks

    percentage = (total_marks / 500) * 100
    print("Percentage =", percentage)

    total_percentage += percentage

average = total_percentage / Students_Num
print("Average Percentage =", average)