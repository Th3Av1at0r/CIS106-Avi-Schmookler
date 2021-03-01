def displayresult(pay):
    print("your pay this time is $" + str(pay))

def gethours():
    print("How many hours did you work?")
    hours = float(input())
    
    return hours

def getpay(hours, rate):
    if hours > 40:
        pay = rate * 40 + (hours - 40) * (rate * 1.5)
    else:
        pay = rate * hours
    
    return pay

def getrate():
    print("How much to you make per hour?")
    rate = float(input())
    
    return rate

# Main
# This program takes your hours worked and your rate of pay and produces your pay in the time given while calculating for overtime
hours = gethours()
rate = getrate()
pay = getpay(hours, rate)
displayresult(pay)
