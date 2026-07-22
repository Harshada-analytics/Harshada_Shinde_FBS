#Q.3 convert distant given in feet and inches into meterr and centimeter.

#feet = 0.3048 meter 
#inch = 2.54 centimeter

feet = float(input("Enter feet:"))
centimeter = float(input("Enter inches: "))

meter = feet * 0.3048
centimeter = centimeter * 2.54

print("Meter =", meter)
print("Centimetr =", centimeter)
