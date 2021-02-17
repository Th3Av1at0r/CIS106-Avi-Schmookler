def getdogname():
    
    print("What's your dog's name?")
    dogname = (input())
    
    return dogname
    
def displayresult(dogname,dogage):

    print(str(dogname) + " is " + str(dogage) + " years old in dog years")
    
def getdogage():
    
    print("How many years old is your dog?")

    humandogage = float(input())
    dogage = humandogage *7
    
    return dogage

# Main
# This program takes your dogs name and age
# and gives you the age in dog years

dogname = getdogname()
dogage = getdogage()
displayresult(dogname, dogage)
