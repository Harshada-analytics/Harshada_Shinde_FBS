#Q3. Create a class Shirt with members as sid,sname,type(formal etc), price and
#size(small,large etc) .Add following methods:
#j. Constructor (Support both parameterized and parameterless)
#k. Destructor
#l. ShowBook
#m. For each size of shirt price should change by 10%.
#(eg. If 1000 is price then small price = 1000, medium = 1100,large=1200 and
#xlarge=1300) Use static concept.

class shirt():

    def __init__(self, sid=None, sname=None, type=None, price=None, size=None):
        self.sid = sid
        self.sname = sname
        self.type = type
        self.price = price
        self.size = size 

    def changePrice(self):

        if (self.size == "small") :
            self.price = self.price

        elif self.size == "medium" :
            self.price = self.price + (self.price * 10/100)
              
        elif self.size == "large" :
            self.price = self.price + (self.price * 20 / 100)

        elif self.size == "x-large" :
            self.price = self.price + (self.price * 30 / 100)

    def showshirt(self):
        print(f"id: {self.sid}, Name: {self.sname}, Type: {self.type}, price: {self.price}, size: {self.size}")

    def __del__(self):
        print("This is distructor")

s1 = shirt(111, "shirt", "Formal", 1000, "small")
s1.changePrice()          #change price according to size
s1.showshirt()

print("------------------------------------------------")

s2 = shirt()
s2.showshirt()
