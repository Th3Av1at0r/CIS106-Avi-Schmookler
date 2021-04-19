# this program asks for values seperated by commas
# and prints them on seperate lines

def get_values():
    values = input("Please enter values separated by commas.\n")
    
    return values
    
    
def get_final_values(values):
    seperate_values = values.replace(",", " ")
    final_values = seperate_values.split()
    
    return final_values
    
    
def display_result(final_values):
    for elem in final_values:
        print(elem)
    
    
def main():
    values = get_values()
    final_values = get_final_values(values)
    display_result(final_values)
    

main()
