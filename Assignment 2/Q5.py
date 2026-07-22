#Q.5 Write a program to calculate selling price of book based on cost, price and discount.

#take input 
cost_price = float(input("Enter cost price of book :"))
discount = float(input("Enter discount percentage :"))

#perform operation(calculation)

discount_amount = (cost_price * discount)/100
selling_price = cost_price - discount_amount 


#display output
print("selling price of book = ", selling_price)