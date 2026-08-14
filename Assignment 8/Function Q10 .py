#Q10. Write a program to check if entered year is leap or not.

def leap_year(years):

    if (year % 400 == 0): #or (year % 4 == 0 and year % 100 != 0):
        print("Leap Year",year)
    else:
        print("Not Leap Year")
  
year = int(input("Enter Year : "))
leap_year(year)