# this program takes the user's first and last name and transfers it into the 
# format of Lastname, first initial.

def get_full_name():
    full_name = input("what is your first and last name?\n")
    
    return full_name
    
    
def get_name(full_name):
    name = full_name.split()
    if (len(name) <= 1 or len(name) >= 3):
        print("That is not a valid input, exiting code")
        exit()
    else:
        return name


def get_first_initial(name):
    first_initial = name[0]
    
    return first_initial


def display_result(name, first_initial):
    first_initial = name[0]
    print(name[1] + ", " + first_initial[0] + ".")
    
    
def main():
    full_name = get_full_name()
    name = get_name(full_name)
    first_initial = get_first_initial(name)
    display_result(name, first_initial)
    
main()
