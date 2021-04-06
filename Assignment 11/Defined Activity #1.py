# This program gives you the name of the month and number
# of days in it when the user inputs the year and month number

def get_year():
    year = int(input("What year are we looking into?\n"))
    
    if (0 >= year):
        print("That is not a valid input, exiting code.")
        exit()
    
    return year


def get_month():
    month_number = int(input("And what month in that year?\n"))
    month_number = (month_number - 1)
    
    if (0 > month_number or month_number > 12):
        print("That is not a valid input, exiting code.")
        exit()

    months_array = (['January', 'February', 'March', 'April', 'May', 
        'June', 'July', 'August', 'September', 'October',
        'November', 'December'])
    month = months_array[month_number]
    
    return month


def get_days(year, month):
    if month == 'January':
        days = 31
        
        return days
        
    elif month == 'February':
        if ((year % 4) == 0):
            if ((year % 100) == 0):
                if ((year % 400) == 0):
                    days = 29
                    
                    return days
                    
                else:
                    days = 28
                    
                    return days
            else:
                days = 29
                    
                return days
        else:
            days = 28
                    
            return days
            
    elif month == 'March':
        days = 31
        
        return days
        
    elif month == 'April':
        days = 30
        
        return days
        
    elif month == 'May':
        days = 31
    
        return days
    
    elif month == 'June':
        days = 30
    
        return days
    
    elif month == 'July':
        days = 31
    
        return days
    
    elif month == 'August':
        days = 31
    
        return days
    
    elif month == 'September':
        days = 30
    
        return days
    
    elif month == 'October':
        days = 31
    
        return days
    
    elif month == 'November':
        days = 30
    
        return days
    
    elif month == 'December':
        days = 31
        
        return days

    
def display_result(year, month, days):
    print(str(month) + " " + str(year) + " had " + str(days) + " days")

    
def main():
    while True:
        year = get_year()
        month = get_month()
        days = get_days(year, month)
        display_result(year, month, days)
    
    
main()
