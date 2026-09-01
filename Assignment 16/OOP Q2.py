#Q2.Create a class Product with members as pid,pname,price and quantity .Add
#following methods:
#e. Constructor (Support both parameterized and parameterless)
#f. Destructor
#g. ShowBook
#h. Add static member discount.
#i. Provide methods for applying discount on price of product.

class Product():

    count = 0
    Product_discount = 10  #Static/class member

    def __init__(self, pid=None,pname=None,price=None,quantity=None):
        self.pid = pid
        self.pname = pname
        self.price = price
        self.quantity = quantity 

        Product.count +=1

    def showProduct(self): 
        print(f"id: {self.pid}, name: {self.pname}, price: {self.price}, quantity: {self.quantity} ")
        
    def __del__(self):
        print("This is a destructor")

    def applyDiscount(self):
        self.price = self.price - (self.price * 10 / 100)

p1 = Product(102, "XYZ", 450, 5)
p1.showProduct()

print("----------------------------------------------")

p1.applyDiscount()
print("Price after discount:", p1.price)

print("------------------------------------------------")

p2 = Product()
p2.showProduct()

print("--------------------------------------------------")

print("Total objects created:", Product.count)
