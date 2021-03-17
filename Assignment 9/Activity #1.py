# this program takes grades that the user
# inputs and adds them up untill the user
# enters a negative value

def get_total():
    counter = 0
    old_score = 0
    new_score = 0
    while True:
        old_score = new_score
        score = get_score()
        new_score = old_score + score
        counter += 1
        if not(score >= 1): break
    average = get_average(new_score, score, counter)
    total = average
    
    return total
    
    
def get_average(new_score, score, counter):
    average = (new_score - score) / (counter - 1)

    return average


def display_results(total):
    print("your class' average is " + str(total))


def get_score():
    print("please enter a score")
    score = int(input())

    return score


def main():
    total = get_total()
    display_results(total)
    
main()
