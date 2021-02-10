# When you gove my program a length and height it gives you the area of
# a parallellagram, a triangle and a circle with the given dimentions 

print ("What is the Length?")
Length = float(input())
print ("What is the Height?")
Height = float(input())

Parallellagram = Length * Height
Triangle = Parallellagram / 2
Radius = Height / 2
import math
Circle = Radius * Radius * math.pi

print ("your dimensions as a Parallellagram is " + str(Parallellagram))
print ("your dimensions as a Triangle is " + str(Triangle))
print ("your dimensions as a Circle is " + str(Circle))
