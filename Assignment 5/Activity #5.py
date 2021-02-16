def yards(length, width):
    areainyards = length * width / 9
    
    return areainyards

# Main
# This program takes length and width in feet and gives
# area in yards
print("How many Feet in the Length?")
length = float(input())
print("How many Feet in the Width?")
width = float(input())
areainyards = yards(length, width)
print("The area in yards is " + str(areainyards))
