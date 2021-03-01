print("How many hours did you work?")
hours = float(input())
print("How much to you make per hour?")
rate = float(input())
if hours > 40:
    pay = rate * 40 + (hours - 40) * (rate * 1.5)
    print("your getting paid $" + str(pay))
else:
    pay = rate * hours
    print("your getting paid $" + str(pay))
