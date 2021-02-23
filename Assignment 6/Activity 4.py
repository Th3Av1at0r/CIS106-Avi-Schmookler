# This program was beautified by:
# tutorialspoint "online formatter"
# This program takes your base and height
# and gives you the area of a parallellogram
# and a triangle with the same dimensions

def display_result(parallellogram_area, triangle_area):
    
    print("Your area as a parallellogram is " 
          
    + str(parallellogram_area)
          
    + "Your area as a triangle is "
          
    + str(triangle_area))
    
    
def get_base():
    
    print("What's your base?")
    base = float(input())

    return base
    
    
def get_height():
    
    print("What's your height?")
    height = float(input())

    return height
    
    
def get_parallellogram_area(base, height):
    
    parallellogram_area = base * height
    
    return parallellogram_area
    
    
def get_triangle_area(parallellogram_area):
    
    triangle_area = parallellogram_area / 2
    
    return triangle_area
    
    
# main
def main():
    
    base = get_base()
    height = get_height()
    parallellogram_area = get_parallellogram_area(base, height)
    triangle_area = get_triangle_area(parallellogram_area)
    display_result(parallellogram_area, triangle_area)


main()
