#Q3. WAP to find sum of followig series using functions.
#a. 1+ 2 + 3 + 4+..... + n

def sum (num):
    
    total = 0
    
    for i in range(1, num+1):
        total = total + i 

    return total
num = int(input("Enter Number :"))
res = sum(num)

print("Total :",res)