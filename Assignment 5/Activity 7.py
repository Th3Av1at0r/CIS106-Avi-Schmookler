def dogyear(age):
    dogyears = age * 7
    
    return dogyears
    
# Main
# This program takes your dogs name and age
# and gives you the age in dog years


print("What's your dog's name?")
name =(input())

print("How many years old is your dog?")
age = float(input())

dogage = dogyear(age)

print(str(name) + " is " + str(dogage) + " years old in dog years")
