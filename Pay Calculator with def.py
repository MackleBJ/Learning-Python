#Pay Calculator with Def computepay()


def computepay(hrs, rate):
    if hrs <= 40:
        wages=hrs*rate
        return wages
    else:
        wages=40*rate+((hrs-40)*(rate*1.5))
        return wages

hrs=float(input("Enter number of hours worked:"))
rate=float(input("Enter hourly wages:"))

wages=computepay(hrs,rate)
print("Pay", wages)
