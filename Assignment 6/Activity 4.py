# This program was beautified by:
# tutorialspoint "online formatter"
# This program takes your length and width
# and gives you the area of a parallellogram
# and a triangle with the same dimensions

def display_result(parallellogram_area, triangle_area):
    
    print ("Your area as a parallellogram is " \
    + str(parallellogram_area))
    
    print ("Your area as a triangle is " \
    + str(triangle_area))
    
    
def get_length():
    
    print ("What's your length?")
    length = float(input())

    return length
    
def get_width():
    
    print ("What's your width?")
    width = float(input())

    return width
    
def get_parallellogram_area(length, width):
    
    parallellogram_area = length * width
    
    return parallellogram_area
    
def get_triangle_area(parallellogram_area):
    
    triangle_area = parallellogram_area / 2
    
    return triangle_area
    
    
# main
def main():
    
    length = get_length()
    width = get_width()
    parallellogram_area = get_parallellogram_area(length, width)
    triangle_area = get_triangle_area(parallellogram_area)
    display_result(parallellogram_area, triangle_area)


main()
