#Q4. Write a program to enter P, T, R and calculate Simple Intreast.

#Take input
principal= int(input("Enter principal :"))
Rate = int(input("Enter Rate (%):"))
Time = int(input("Enter Time(years):")) 

#Perform Operation
# S.I = P*T*R/100=900
simple_intrest = (principal*Rate*Time)/100

#Display Output
print("Simple Interest :", simple_intrest)


#principal 10 pasun start honari value ghetli tr error yet.