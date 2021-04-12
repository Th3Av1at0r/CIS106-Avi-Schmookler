# This program takes a list of grades, puts them into an array
# then figueres out the highest, lowest, and average of the list

def get_grades():
    grades = list()
    print('Please enter the grades of the class: \n')
    while True:
        grade_input = input("grade:")
        grades.append(int(grade_input))
        if not(int(grade_input) >= 0):
            grades.remove(int(grade_input))
            break
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


def get_average_grade(grades):
    average_grade = 0
    for number in range(0, len(grades)):    
        average_grade = average_grade + grades[number]
    average_grade = (int(average_grade) / len(grades))
    
    return average_grade
    
    
def display_results(highest_grade, lowest_grade, average_grade):
    print("for your class' grades the highest was " + str(highest_grade) +
    " and your lowest grade was " + str(lowest_grade) + 
    ". The class average was " + str(average_grade))
    
    
def main():
    grades = get_grades()
    highest_grade = get_highest_grade(grades)
    lowest_grade = get_lowest_grade(grades)
    average_grade = get_average_grade(grades)
    display_results(highest_grade, lowest_grade, average_grade)
    
    
main()
