# When you gove my program a length and height it gives you the area of
# a parallellagram, a triangle and a circle with the given dimentions 

import math

print("What is the Base?")
base = float(input())
print("What is the Height?")
height = float(input())
print("What is theRadius?")
radius = float(input())

parallellogram = base * height
triangle = parallellogram / 2
circle = radius * radius * math.pi

print("your area as a Parallellogram is " + str(parallellogram))
print("your area as a Triangle is " + str(triangle))
print("your area as a Circle is " + str(circle))
