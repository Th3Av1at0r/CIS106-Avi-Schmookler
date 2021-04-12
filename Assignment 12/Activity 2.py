# when the user thinks of a number, this program guesses a new number higher 
# or lower based on the user's input untill it is equal to the user's number

def calculate_guess():
    highest = 100
    lowest = 0
    count = 0
    guesses = []
    while True:
        newnumber = get_new_number(highest, lowest)
        guess = newnumber
        guesses.append(guess)
        count = count + 1

        correct = get_correct(guess)
        if correct == "h":
            lowest = guess + 1
        elif correct == "l":
            highest = guess - 1
        else:
            display_result(correct, count, guesses)
        if not(correct != "e"): 
            break


def display_result(correct, count, guesses):
    if correct == "e":
        print("Yay that was the correct number!")
        print("And it only took " + str(count) + " guesses!")
        print("the guesses were " + str(guesses))
    else:
        print("That is not a valid input")
        
        
def get_correct(guess):
    print("Is it (h)igher, (l)ower, or (e)qual to " + str(guess) + " ?")
    correct = input()
    
    return correct
    
    
def get_new_number(highest, lowest):
    newnumber = int(float(highest + lowest) / 2)
    return newnumber
    
    
def main():
    calculate_guess()


main()
