def is_leap_year(year):
    if year % 4 == 0 and year % 400 == 0:
        return True
    else:
        return False
        
is_leap_year(2400) 