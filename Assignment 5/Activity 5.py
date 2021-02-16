# this program takes length and width
# and gives you area in feet and yards
print ("How many Feet in the Length?")
length = float(input())
print ("How many Feet in the width?")
width = float(input())
areainfeet = length * width
print ("your area in feet is" + str(areainfeet))
areainyards = float(areainfeet) / 9
print ("your area in yards is" + str(areainyards))
