#Q3. Write a program to accept distance in km and convert it into meters and
#centimeters both.

km = float(input("Enter distance in km: "))

meter = km * 1000
centimeter = km * 100000

print("Distance in meter:", meter)
print("Distance in centimeter:", centimeter)