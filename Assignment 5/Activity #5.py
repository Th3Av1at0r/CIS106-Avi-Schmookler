def calculatearea(length):
    print("what is the width in feet")
    width = float(input())
    feetarea = length * width
    
    return feetarea

def displayresult(feetarea):
    yardsarea = feetarea / 9
    print("your area in yards is " + str(yardsarea))

def getlength():
    print("What is the length in feet?")
    length = float(input())
    
    return length

# Main
# This program takes length and width in feet
# and it outputs area in yards
length = getlength()
feetarea = calculatearea(length)
displayresult(feetarea)
