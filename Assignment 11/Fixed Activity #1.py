# This program takes a list of grades, puts them into an array
# then figueres out the highest, lowest, and average of the list

def get_number_of_grades():
    number_of_grades = input("How many grades would you like to enter? \n")

    return number_of_grades
    
    
def get_grades(number_of_grades):
    grades = []
    print('Please enter the grades: \n')
    for number in range(int(number_of_grades)):
        grade_input = input("grade:")
        grades += [int(grade_input)]
    print('Your grades are: ', grades)
    
    return grades
    

def get_highest_grade(grades):
    highest_grade = grades[0]    
    for number in range(0, len(grades)):    
        if(grades[number] > highest_grade):    
            highest_grade = grades[number]    
    
    return highest_grade
    
    
def get_lowest_grade(grades):
    lowest_grade = grades[0] 
    for number in range(0, len(grades)):    
        if(grades[number] < lowest_grade):    
            lowest_grade = grades[number]   
    
    return lowest_grade


def get_average_grade(grades, number_of_grades):
    average_grade = 0
    for number in range(0, len(grades)):    
        average_grade = average_grade + grades[number]
    average_grade = (int(average_grade) / int(number_of_grades))
    
    return average_grade
    
    
def display_results(highest_grade, lowest_grade, average_grade):
    print("for your class' grades the highest was " + str(highest_grade) +
    " and your lowest grade was " + str(lowest_grade) + 
    ". The class average was " + str(average_grade))
    
    
def main():
    number_of_grades = get_number_of_grades()
    grades = get_grades(number_of_grades)
    highest_grade = get_highest_grade(grades)
    lowest_grade = get_lowest_grade(grades)
    average_grade = get_average_grade(grades, number_of_grades)
    display_results(highest_grade, lowest_grade, average_grade)
    
    
main()
