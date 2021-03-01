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
    
    
def get_m_d_h_s():
     
    variable = 0
     
    while variable == 0:
    
        print("do you want to know how old you are in (M)onths, " + 
        "(D)ays, (H)ours, or (S)econds?")
    
        m_d_h_s = input()
        
        if m_d_h_s.upper() in ("M", "D", "H", "S"):
        
            return m_d_h_s.upper()
        
        else:
            print("that is not a valid input")
            continue
    
    
def get_m(years):
    
    m = years * 12
    
    return m
    
    
def get_d(years):
    
    d = years * 365
    
    return d
    
    
def get_h(years):
    
    h = years * 8760
    
    return h
    
    
def get_s(years):
    
    s = years * 31536000
    
    return s


def get_m_d_h_s_result(m_d_h_s):
    
    if m_d_h_s == "M":
        return "months"
    elif m_d_h_s == "D":
        return "days"
    elif m_d_h_s == "H":
        return "hours"
    elif m_d_h_s == "S":
        return "seconds"


def display_result(m_d_h_s, m_d_h_s_result):
    
    print("your age in " + str(m_d_h_s_result) + " is " +
        str(m_d_h_s))
    
    
# main
def main():
    
    years = get_years()
    m_d_h_s = get_m_d_h_s()
    m_d_h_s_result = get_m_d_h_s_result(m_d_h_s)
    if m_d_h_s == "M":
        m = get_m(years)
        display_result(m, m_d_h_s_result)
    elif m_d_h_s == "D":
        d = get_d(years)
        display_result(d, m_d_h_s_result)
    elif m_d_h_s == "H":
        h = get_h(years)
        display_result(h, m_d_h_s_result)
    elif m_d_h_s == "S":
        s = get_s(years)
        display_result(s, m_d_h_s_result)
    

main()
