#Comment - Neal Stack
#This is my python program to calculate tuition owed based on district code and credit hours
def f_towe(chrs, dcode):
    if dcode == "I":
        crcost = 250
    else:
        crcost = 550
    towe = chrs * crcost
    return towe
tottowe = 0
sc = 0
r = input("Would you like to calculate tuition cost (y/n)? ")
while r == "y":
    lame = input("Enter your last name: ")
    chrs = int(input("Enter your credit hours taken: "))
    dcode = str(input("Enter your district code: "))
    towe = f_towe(chrs, dcode)
    tottowe = tottowe + towe
    sc = sc + 1
    print("Student last name is: ",lame)
    outtxt = f"Tuition owed by student is: ${towe:.2f}"
    print(outtxt)
    r = input("Would you like to calculate another tuition cost (y/n)? ")
print("Total students is: ",sc)
outtxt = f"Total tuition owed is ${tottowe:.2f}"
print(outtxt)