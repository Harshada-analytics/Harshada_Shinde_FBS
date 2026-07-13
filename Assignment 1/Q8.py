#Q8. write a program to convert days into years, weeks and days.

#Take Input
days= int(input("Enter days :"))

#Total days // 365
years = days//365
print(years)

days = days % 365 
print(days)

weeks = days // 7
print(weeks)

days = days % 7
print(days)


#display output 
print(f'Years:{years}, Weeks:{weeks}, Days:{days}.')