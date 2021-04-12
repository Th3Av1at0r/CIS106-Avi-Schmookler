# when the user thinks of a number, this program guesses a new number higher 
# or lower based on the user's input untill it is equal to the user's number

def calculate_guess():
    guess = 50
    highest = 100
    lowest = 0
    correct = "ne"
    count = 1
    guesses = list()
    guesses.append(50)
    while True:
        correct = get_correct(guess)
        if correct == "h":
            lowest = guess
            newnumber = get_new_number(correct, highest, lowest, guess)
            guess = newnumber
            guesses.append(guess)
        else:
            if correct == "l":
                highest = guess
                newnumber = get_new_number(correct, highest, lowest, guess)
                guess = newnumber
                guesses.append(guess)
            else:
                display_result(correct, count, guesses)
        count = count + 1
        if not(correct != "e"): break


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
    
    
def get_new_number(correct, highest, lowest, guess):
    if correct == "h":
        newnumber = guess + int(float(highest - lowest) / 2)
    else:
        newnumber = guess - int(float(highest - lowest) / 2)
    
    return newnumber
    
    
def main():
    calculate_guess()


main()
