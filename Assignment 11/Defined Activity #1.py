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
    
    if (0 >= month_number <= 13):
        print("That is not a valid input, exiting code.")
        exit()
    
    import numpy as np

    months_array = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
        'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
    month = (months_array[month_number])
    
    return month


def get_days(year, month):
    if month == 'Jan':
        days = 31
        
        return days
        
    elif month == 'Feb':
        if ((year % 4) == 0):
            days = 29
            
            return days
            
        else:
            days = 28
            
            return days
            
    elif month == 'Mar':
        days = 31
        
        return days
        
    elif month == 'Apr':
        days = 30
        
        return days
        
    elif month == 'May':
        days = 31
    
        return days
    
    elif month == 'Jun':
        days = 30
    
        return days
    
    elif month == 'Jul':
        days = 31
    
        return days
    
    elif month == 'Aug':
        days = 31
    
        return days
    
    elif month == 'Sep':
        days = 30
    
        return days
    
    elif month == 'Oct':
        days = 31
    
        return days
    
    elif month == 'Nov':
        days = 30
    
        return days
    
    elif month == 'Dec':
        days = 31
        
        return days

    
def display_result(year, month, days):
    print(str(month) + " " + str(year) + " had " + str(days) + " days")

    
def main():
    while (1 == 1):
        year = get_year()
        month = get_month()
        days = get_days(year, month)
        display_result(year, month, days)
    
    
main()
