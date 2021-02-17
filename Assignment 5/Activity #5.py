def displayresult(yardsarea):
    print("your area in yards is " + str(yardsarea))

def getfeetarea(length, width):
    feetarea = length * width
    
    return feetarea

def getlength():
    print("What is the length in feet?")
    length = float(input())
    
    return length

def getwidth():
    print("What is the width in feet?")
    width = float(input())
    
    return width

def getyardsarea(feetarea):
    yardsarea = feetarea / 9
    
    return yardsarea

# Main
# This program takes length and width in feet
# and it outputs area in yards
length = getlength()
width = getwidth()
feetarea = getfeetarea(length, width)
yardsarea = getyardsarea(feetarea)
displayresult(yardsarea)
