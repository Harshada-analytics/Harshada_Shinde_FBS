#Q2.Write a program to calculate simple interest based on Principal, Rate and Time
#(SI = P*R*T/100)

P = float(input("Enter Principle:"))
R = float(input("Enter Rate:"))
T = float(input("Enetr Time:"))

SI = P * R * T / 100

print("Simple Interest:", SI)