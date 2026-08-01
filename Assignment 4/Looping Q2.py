
#Q2. WAP to print all odd numbers until n .

num= int(input("Enter Numbers :"))
i = 0
while(i <= num):
     if(i % 2 != 0):
        print("Odd Numbers:", i)
     i+=1