#Q11. Accept age of five people and also per person ticket amount and then calculate total
#amount to ticket to travel for all of them based on following condition :

#a. Children below 12 = 30% discount
#b. Senior citizen (above 59) = 50% discount
#c. Others need to pay full.

i= 1
totalprice = 0
while i <= 5:
    ag1 = int(input(f"enter the age of {i} person="))
    tkprice1 = float(input(f"Enter the Ticket price of {i}person="))
    if ag1<12:
        totalprice = totalprice+(tkprice1 * 0.30)
    elif ag1>59:
        totalprice = totalprice+(tkprice1 * 0.50)
    else:
        totalprice = totalprice + tkprice1
    i+=1
print(f"Total price for the Travling is = {totalprice}")
    