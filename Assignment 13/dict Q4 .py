#Q.4 Python Program to Generate a Dictionary that Contains Numbers (between 1 
#and n) in the Form (x,x*x).

num = int(input("Enter Number :"))

dictionary = {}

for i in range(1, num + 1):
    dictionary[i] = i * i

print(dictionary)