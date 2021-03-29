def finish(correct, count):
    if correct == "e":
        print("Yay that was the correct number!")
        print("And it only took " + str(count) + " guesses!")
    else:
        print("That is not a valid input")

def getcorrect(guess):
    print("Is it (h)igher, (l)ower, or (e)qual to " + str(guess) + " ?")
    correct = input()
    
    return correct

def getnewnumber(correct, highest, lowest, guess):
    if correct == "h":
        newnumber = guess + int(float(highest - lowest) / 2)
    else:
        newnumber = guess - int(float(highest - lowest) / 2)
    
    return newnumber

# Main
# This program guesses the random number that the user thinks of. It also has an input validation that is now built into it.
guess = 50
highest = 100
lowest = 0
correct = "ne"
count = 1
while True:    #This simulates a Do Loop
    correct = getcorrect(guess)
    if correct == "h":
        lowest = guess
        newnumber = getnewnumber(correct, highest, lowest, guess)
        guess = newnumber
        count = count + 1
    else:
        if correct == "l":
            highest = guess
            newnumber = getnewnumber(correct, highest, lowest, guess)
            guess = newnumber
            count = count + 1
        else:
            if correct == "e":
                finish(correct, count)
                count = count + 1
            else:
                print("That is not a valid input please try again.")
    if not(correct != "e"): break   #Exit loop
