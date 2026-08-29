#Q1. Create a class book with members as bid, bname, price and author. 
#Add following methods :
#a. Constructor (Support both parameterized and parameterless)
#b. Destructor
#c. Show Book

class Book():
    
    def __init__(self, Bid=None, Bname=None, price=None, author=None): #because of None we got Both parametrized and parameterless
        self.Bid = Bid
        self.Bname = Bname 
        self.price = price
        self.author = author 
    
    def showbook(self):
        print(f"id: {self.Bid}, name: {self.Bname}, price: {self.price}, author: {self.author}")

    def __del__(self):
        print("Its a destructor, mostly no need to use destructor")
    
# parametrized Object
B1 = Book(101, "Chava", 400, "Sambhaji Raje")
B1.showbook()
        
print("---------------------------------------")

# parameterless Object
B2 = Book()
B2.showbook()

        
