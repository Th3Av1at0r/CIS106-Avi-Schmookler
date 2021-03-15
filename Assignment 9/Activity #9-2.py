def getnewnumber(correct, highest, lowest, guess):
    if correct == "h":
        newnumber = guess + float(highest - lowest) / 2
    else:
        newnumber = guess - float(highest - lowest) / 2
    
    return newnumber

def guesscalculation():
    guess = 50
    highest = 100
    lowest = 0
    correct = "ne"
    while True:    #This simulates a Do Loop
        print("Is it (h)igher, (l)ower, or (e)qual to " + str(guess) + " ?")
        correct = input()
        if correct == "h":
            lowest = guess
            newnumber = getnewnumber(correct, highest, lowest, guess)
            guess = newnumber
        else:
            if correct == "l":
                highest = guess
                newnumber = getnewnumber(correct, highest, lowest, guess)
                guess = newnumber
            else:
                if correct == "e":
                    print("Yay that was the correct number!")
                else:
                    notvalid()
        if not(correct != "e"): break   #Exit loop

def notvalid():
    print("That is not a valid input")

def start():
    ready = "Notready"
    while ready != "ready":
        print("Please think of a number between 1 and 100 and say ready when you are ready")
        ready = input()
        if ready == "ready":
            guesscalculation()
        else:
            notvalid()

# Main
# This program guesses the random number that the user thinks of.
start()
