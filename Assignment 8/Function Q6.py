#6. Write a program to find print the following Fibonacci series using
#functions:
#1 1 2 3 5 8 n terms

def fibonacci(num):
    a = 1
    b = 1

    for i in range(num):
        c = a + b
        print(a, end=" ")

        a = b
        b = c

number = int(input("Enter Number of Terms: "))
fibonacci(number)
