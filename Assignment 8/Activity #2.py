# This program takes grades and averages
# them out to calculate the class average
# Jess Elis helped debug this program

def get_number_of_grades():
    print("How many grades do you want to input?")
    number_of_grades = int(input())
    
    return number_of_grades
    

def get_total(number_of_grades):
    counter = 1
    total = 0
    while counter <= number_of_grades:
        score = get_score()
        total += score
        counter += 1
    
    return total 
    
    
def get_score():
    print("please input a score")
    score = float(input())
    
    return score
    

def get_average(total, number_of_grades):
    average = total / number_of_grades
    
    return average
    

def display_result(average):
    print("the class average is " + str(average))
    
    
# main
def main():
    number_of_grades = get_number_of_grades()
    total = get_total(number_of_grades)
    average = get_average(total, number_of_grades)
    display_result(average)
main()
