# This program was beautified by:
# tutorialspoint "online formatter"
# This program takes your hours worked
# and your hourly rate and gives you
# your pay over a week, month, and year

def get_hours():
    
    print("how many hours do you work per week?")
    hours = float(input())
    
    return hours
    
    
def get_rate():
    
    print("what is your hourly rate?")
    rate = float(input())
    
    return rate
   
    
def get_weekly_pay(rate, hours):

    weekly_pay = rate * hours
    
    return weekly_pay
  
    
def get_monthly_pay(yearly_pay):
    
    monthly_pay = yearly_pay / 12
    
    return monthly_pay
  
    
def get_yearly_pay(weekly_pay):
    
    yearly_pay = weekly_pay * 52
    
    return yearly_pay


def display_result(weekly_pay, monthly_pay, yearly_pay):

    print("your pay in a week is $" +
        str(weekly_pay) +
            " your pay in a month is $" +
                str(monthly_pay) +
                    " your pay in a year is $" +
                        str(yearly_pay))

    
# main
def main():
    
    rate = get_rate()
    hours = get_hours()
    weekly_pay = get_weekly_pay(rate, hours)
    yearly_pay = get_yearly_pay(weekly_pay)
    monthly_pay = get_monthly_pay(yearly_pay)
    display_result(weekly_pay, monthly_pay, yearly_pay)
 

main()
