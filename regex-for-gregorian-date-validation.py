import re
date_validator = r'\d\d\.\d\d.\d\d\d\d'

pattern = re.compile(date_validator)



year = date_validator.split([-1])

# calculate leap year

def is_leap_year(year):
    if year%4==0:
        if year%100==0:
            if year%400==0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

is_leap_year = is_leap_year(int(year))

if

if is_leap_year:
