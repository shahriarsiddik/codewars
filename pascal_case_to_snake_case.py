def to_underscore(string):

    camel_string_list = list(str(string))
    camel_string_list[0]=camel_string_list[0].lower()
    for i in range(1,len(camel_string_list)):
        print type(camel_string_list[i])
        if camel_string_list[i].istitle():
            to_lower = camel_string_list[i].lower()
            camel_string_list.insert(i,'_')
            camel_string_list[i+1]=to_lower
    return ''.join(camel_string_list)

print to_underscore(5)