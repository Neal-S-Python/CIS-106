#Comment - Neal Stack
#This is my python program to calculate the miles driven and cost of gas for road trips
def f_mpg(miles, gal):
    mpg = miles / gal
    gascost = gal * 3
    return mpg, gascost
trips = 0
totalmiles = 0
totgascost = 0
r = input("Do you want to calculate trip costs (y/n)? ")
while r == "y":
    dest = input("Enter the destination city: ")
    miles = float(input("Enter miles travelled: "))
    gal = float(input("Enter gallons used for trip: "))
    trips = trips + 1
    mpg, gascost = f_mpg(miles, gal)
    print("Your destination city is: ",dest)
    print("Your miles travelled is: ",miles)
    print("Your gallons used for trip is: ",gal)
    outtxt = f"Your miles per gallon is: {mpg:.2f}"
    print(outtxt)
    outtxt = f"Your trip cost is: ${gascost:.2f}"
    print(outtxt)
    totgascost = totgascost + gascost
    totalmiles = totalmiles + miles
    r = input("Do you want to calculate another trip cost (y/n)? ")
print("Trips taken: ",trips)
print("Total miles driven: ",totalmiles)
outtxt = f"Total cost of gas is ${totgascost:.2f}"
print(outtxt)