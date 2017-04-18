import re
def is_valid_IP(strng):
    # re_check=re.compile('^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$')
    re_check = re.compile(r'^' +
               r'(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9]).' +
               r'(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9]).' +
               r'(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9]).' +
               r'(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])$'
               )
    if re_check.match(strng):
        if len(strng.split('.'))<4:
            return False

        for i in strng.split('.'):
            print i
            if i[0] == '0':
                return False
        return True
    else:
        return False

print is_valid_IP('12,34.56.1')