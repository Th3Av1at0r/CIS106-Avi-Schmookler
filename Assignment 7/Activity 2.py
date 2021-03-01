# this program takes your age 
# in years and gives it back 
# in months, days, hours, or seconds


def get_years():
    
    variable = 0
    
    while variable == 0:
    
        print("how many years old are you?")
    
        years = input()
    
        if years.isdigit():
            return float(years)
        else: 
            print("that is not a valid input")
            continue
    
    
def get_months_days_hours_seconds():
     
    variable = 0
     
    while variable == 0:
    
        print("do you want to know how old you are in (M)onths, " + 
        "(D)ays, (H)ours, or (S)econds?")
    
        months_days_hours_seconds = input().upper()
        
        if months_days_hours_seconds in ("M", "D", "H", "S"):
        
            return months_days_hours_seconds
        
        else:
            print("that is not a valid input")
            continue
    
    
def get_months(years):
    
    months = years * 12
    
    return months
    
    
def get_days(years):
    
    days = years * 365
    
    return days
    
    
def get_hours(years):
    
    hours = years * 8760
    
    return hours
    
    
def get_seconds(years):
    
    seconds = years * 31536000
    
    return seconds


def get_months_days_hours_seconds_result(months_days_hours_seconds):
    
    if months_days_hours_seconds == "M":
        return "months"
    elif months_days_hours_seconds == "D":
        return "days"
    elif months_days_hours_seconds == "H":
        return "hours"
    elif months_days_hours_seconds == "S":
        return "seconds"
    else: 
        print("unknown variable")
    
    
def display_result(months_days_hours_seconds,
                   months_days_hours_seconds_result):
    
    print("your age in " + str(months_days_hours_seconds_result) + " is " +
        str(months_days_hours_seconds))
    
    
# main
def main():
    
    years = get_years()
    months_days_hours_seconds = get_months_days_hours_seconds()
    months_days_hours_seconds_result = \
        get_months_days_hours_seconds_result(months_days_hours_seconds)
    if months_days_hours_seconds == "M":
        months = get_months(years)
        display_result(months, months_days_hours_seconds_result)
    elif months_days_hours_seconds == "D":
        days = get_days(years)
        display_result(days, months_days_hours_seconds_result)
    elif months_days_hours_seconds == "H":
        hours = get_hours(years)
        display_result(hours, months_days_hours_seconds_result)
    elif months_days_hours_seconds == "S":
        seconds = get_seconds(years)
        display_result(seconds, months_days_hours_seconds_result)
    else:
        print("that is not a valid input")
    

main()
