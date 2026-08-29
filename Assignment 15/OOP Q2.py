#Q2. 2. Create a class Product with members as pid,pname,price and quantity .Add
# following methods:
# d. Constructor (Support both parameterized and parameterless)
# e. Destructor
# f. ShowBook

class product():
    def __init__(self, pid=None, pname=None, price=None, quantiy=None):
        self.pid = pid 
        self.pname = pname
        self.price = price
        self.quantity = quantiy

    def showProduct(self):
        print(f"id: {self.pid}, name: {self.pname}, price: {self.price}, Quantity: {self.quantity}")

    def __del__(self):
        print("it's a constructor")

p1 = product(101, "xyz", 500, 4)
p1.showProduct()

print("--------------------------------------------")

p2 = product()
p2.showProduct()
