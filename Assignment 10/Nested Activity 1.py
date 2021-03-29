# This program gives you multiplication tables
# in the form of text, the size of the table
# is up to the user's input


def get_start():
    print("Where do you want the table to start?")
    start = input()
    
    return int(start)
    
    
def get_end():
    print("Where do you want the table to end?")
    end = input()
    
    return int(end)
    
    
def get_length(end, start):
    length = end - start + 1
    
    return length
    
    
def get_if_line_1(start, end, length):
    counter = 1
    
    while True:
        counter = get_line_1(start, end, counter)
        if not(counter == 1):
            get_table(start, end, length, counter)
            break


def get_line_1(start, end, counter):
    for number in range(start, (end + 1)):
        print("\t", number, end = "")
    counter = 2
        
    return counter


def get_table(start, end, length, counter):
    if counter != length:
        print("\n")
        for number_a in range(start, end + 1):
            print(number_a)
            for number_b in range(start, end + 1):
                print("\t", number_a * number_b, end = "")
            print("\n")
    else:
        print("something is broken.")


def main():
    start = get_start()
    end = get_end()
    length = get_length(start, end)
    get_if_line_1(start, end, length)


main()
