# This program gives you the name of the month and number
# of days in it when the user inputs the year and month number

def get_year():
    year = int(input("What year are we looking into?\n"))
    
    if (0 >= year):
        print("That is not a valid input, exiting code.")
        exit()
    
    return year


def get_month_number():
    month_number = int(input("And what month in that year?\n"))
    month_number = (month_number - 1)
    
    if (0 > month_number or month_number > 11):
        print("That is not a valid input, exiting code.")
        exit()
    
    return month_number
    

def get_months_array(year):
    months_array = (['January', 'February', 'March', 'April', 'May', 
        'June', 'July', 'August', 'September', 'October',
        'November', 'December'])
    
    return months_array
    
    
def get_month_name(month_number, months_array):
    month_name = months_array[month_number]
    
    return month_name


def get_days(year, month_number, months_array):
    months_array[0] = 31
    if ((year % 4) == 0):
        if ((year % 100) == 0):
            if ((year % 400) == 0):
                months_array[1] = 29
            else:
                months_array[1] = 28
        else:
            months_array[1] = 29
    else:
        months_array[1] = 28
    months_array[2] = 31
    months_array[3] = 30
    months_array[4] = 31
    months_array[5] = 30
    months_array[6] = 31
    months_array[7] = 31
    months_array[8] = 30
    months_array[9] = 31
    months_array[10] = 30
    months_array[11] = 31
    
    days = months_array[month_number]
    
    return days

    
def display_result(year, month_name, days):
    print(str(month_name) + " " + str(year) + " had " + str(days) + " days")

    
def main():
    while True:
        year = get_year()
        month_number = get_month_number()
        months_array = get_months_array(year)
        month_name = get_month_name(month_number, months_array)
        days = get_days(year, month_number, months_array)
        display_result(year, month_name, days)
    
    
main()
