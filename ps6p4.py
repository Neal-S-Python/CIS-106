#Comment - Neal Stack
#This is my python program to calculate gross pay based on job code and possible overtime bonus
def f_payrate(jobcode):
    if jobcode == "L":
        payrate = 25
    elif jobcode == "A":
        payrate = 30
    elif jobcode == "J":
        payrate = 50
    if hrs > 40:
        grosspay = (payrate * 40) + ((hrs - 40) * (payrate * 1.5))
    else:
        grosspay = payrate * hrs
    return payrate, grosspay
totgrosspay = 0
ec = 0
r = input("Would you like to calculate gross pay (y/n)? ")
while r == "y":
    lname = input("Enter employee last name: ")
    jobcode = str(input("Enter job code: "))
    hrs = float(input("Enter hours worked: "))
    payrate, grosspay = f_payrate(jobcode)
    print("Employee last name is: ",lname)
    print("Hours worked: ",hrs)
    print("Job code is: ",jobcode)
    outtxt = f"Gross pay is ${grosspay:.2f}"
    print(outtxt)
    ec = ec + 1
    totgrosspay = totgrosspay + grosspay
    r = input("Do you want to calculate another gross pay (y/n)? ")
print("Employee's calculated: ",ec)
outtxt = f"Total gross pay is ${totgrosspay:.2f}"
print(outtxt)