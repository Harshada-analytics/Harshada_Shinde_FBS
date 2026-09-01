#Create a class Book with members as bid,bname,price and author.Add following
#methods:
#a. Constructor (Support both parameterized and parameterless)
#b. Destructor
#c. ShowBook
#d. Add static variable count and also maintain count of objects created.

class Book():

    count = 0 #static /class variable

    def __init__(self, Bid=None, Bname=None, price=None, author=None):
        self.Bid = Bid
        self.Bname = Bname
        self.price = price
        self.author = author

        Book.count += 1     #Increases object when object is created

    def showbook(self):
        print(f"id: {self.Bid}, Name: {self.Bname}, price: {self.price}, Author: {self.author}")

    def __del__(self):
        print("This is destructor")

b1 = Book(101, "Mindset", 300, "Harsha")
b1.showbook()

print("-------------------------------------")

b2 = Book()
b2.showbook()