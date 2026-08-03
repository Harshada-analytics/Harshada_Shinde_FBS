#e. X - x2/3 + x3/5 - x47 + ...to n terms

x = int(input("Enter the number ="))
n = int(input("Enter the Ending value ="))

dem= 1
sign= 1
sum= 0 
for i in range(1, n+1):
    sum+=sign*((x**i)/dem)
    dem += 2
    sign*=-1
print(f"sum of series = {sum}")