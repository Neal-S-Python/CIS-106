#Comment - Neal Stack
#This is my python program to calculate batting averages
def f_batavg(hits, atbat):
    batavg = hits / atbat
    return batavg
pc = 0
r = input("Do you want to calculate batting average (y/n)? ")
while r == "y":
    lname = input("Enter players last name: ")
    hits = int(input("Enter number of hits: "))
    atbat = int(input("Enter number of at-bats: "))
    pc = pc + 1
    batavg = f_batavg(hits, atbat)
    outtxt = f"batting average is {batavg:.3f}"
    print(outtxt)
    r = input("Do you want to calculate another batting average (y/n)? ")
print("Number of Players calculated is: ",pc)
