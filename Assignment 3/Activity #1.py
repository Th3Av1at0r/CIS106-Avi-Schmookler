print("How many Hours do you work per week?")
hRS = int(input())
print("What is your Hourly Pay Rate?")
hPR = float(input())
gPW = hPR * hRS
gPY = gPW * 52
print("Your Gross Pay is $" + str(gPW) + " per Week and your Gross Pay per Year is $" + str(gPY))
