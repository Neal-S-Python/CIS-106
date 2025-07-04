#Comment - Neal Stack
#This is my python program using a function to calculate extended price with a potential discount
def f_extprice(qty, unitprice):
    extprice = qty * unitprice
    if extprice > 10000:
        disc = extprice * 0.10
    else:
        disc = 0
    newextprice = extprice - disc
    return newextprice
totalextprice = 0
r = input("Do you want to compute extended price (y/n)? ")
while r == "y":
    qty = int(input("Enter quantity: "))
    unitprice = float(input("Enter unit price: "))
    extprice = f_extprice(qty, unitprice)
    totalextprice = totalextprice + extprice
    outtxt = f"Your total is ${extprice:.2f}"
    print(outtxt)
    r = input("Do you want to compute another extended price (y/n)? ")
outtxt = f"Your total is ${totalextprice:.2f}"
print(outtxt)