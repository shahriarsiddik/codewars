import re

def is_valid_coordinates(coordinates):
    try:
        for i in coordinates.split(','):
            if not re.search('[a-zA-Z]', i):
                return False
        my_list =[float(i) for i in coordinates.split(',')]
        print my_list
        if len(my_list)>2:
            return False
        else:
            if my_list[0]>=-90.0 and my_list[0]<=90.0 and my_list[1]>=-180 and my_list[1]<=180:
                return True
            else:
                return False
    except:
        return False



print is_valid_coordinates("23.245, 11e")