print("How old are you in Years?")

# This program gives you your age in months, days, hours, muinets, and seconds I added the hours, munites, and seconds because I was interested in my own
yRS = int(input())
mTH = yRS * 12
dYS = yRS * 365
hRS = dYS * 24
mIN = hRS * 60
sEC = mIN * 60
print("Your age on your birthday is " + str(mTH) + " Months or " + str(dYS) + " Days or " + str(hRS) + " Hours or " + str(mIN) + " Munites or " + str(sEC) + " Seconds")
