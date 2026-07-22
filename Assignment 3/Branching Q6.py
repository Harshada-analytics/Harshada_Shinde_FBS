#Q6. Write a program to calculate profit or loss.

selling_price = int(input("Enter S.P :"))
Cost_price = int(input("Enter C.P:"))

if(selling_price > Cost_price):
    print("Profit :", selling_price - Cost_price)

elif(Cost_price > selling_price):
    print("loss :",Cost_price - selling_price)

else:
    print("No profit", "No loss")  