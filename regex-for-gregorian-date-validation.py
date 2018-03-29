

import re
date_validator = r'\d\d\.\d\d\.\d\d\d\d'
# date_validator = '(\d{2})[/.-](\d{12})[/.-](\d{4})$'
# email_validator = r'^[a-zA-Z0-9_.-]'

# compare = r'15.14.2009'

pattern = re.compile(compare)

matches = pattern.finditer(date_validator)

for match in matches:
    print(match)

# year = date_validator.split([-1])
# mat =re.match('', date_validator)
# if re.match(date_validator, '15.12.2009'):
#     print('True')
# else:
#     print('False')
# print(re.match(date_validator,))


# calculate leap year
#
# def is_leap_year(year):
#     if year%4==0:
#         if year%100==0:
#             if year%400==0:
#                 return True
#             else:
#                 return False
#         else:
#             return True
#     else:
#         return False
#
# is_leap_year = is_leap_year(int(year))
#
# if

# if is_leap_year:
