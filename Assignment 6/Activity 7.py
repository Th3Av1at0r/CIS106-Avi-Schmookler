# This program was beautified by:
# tutorialspoint "online formatter"
# This program takes your dogs name and age
# and gives you the age in dog years


def get_dog_name():

    print ("What's your dog's name?")
    dog_name = input()

    return dog_name


def display_result(dog_name, dog_age):

    print (str(dog_name) + ' is ' + str(dog_age) \
        + ' years old in dog years')


def get_human_dog_age():

    print ('How many years old is your dog?')

    human_dog_age = float(input())

    return human_dog_age


def get_dog_age(human_dog_age):

    dog_age = human_dog_age * 7

    return dog_age


# Main

def main():

    dog_name = get_dog_name()
    human_dog_age = get_human_dog_age()
    dog_age = get_dog_age(human_dog_age)
    display_result(dog_name, dog_age)


main()
