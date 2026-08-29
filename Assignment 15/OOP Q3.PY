#Q3 Create a class Shirt with members as sid,sname,type(formal etc), price and
#size(small,large etc) .Add following methods:
#g. Constructor (Support both parameterized and parameterless)
#h. Destructor
#i. ShowBook

class shirt():
    def __init__(self, sid=None, sname=None, type=None, price=None, size=None):
        self.sid = sid
        self.sname = sname 
        self.type = type
        self.price = price
        self.size = size

    def showShirt(self):
        print(f"id= {self.sid}, name = {self.sname}, type = {self.type}, price = {self.price}, size = {self.size}")

s1 = shirt(12, "abc", "formal", 400, 30 )
s1.showShirt()

print("====================================================")

s2 = shirt()
s2.showShirt()