def first_non_repeating_letter(string):
    lower_inp_list = list(string.lower())
    string_list = list(string)
    for i in string_list:
        if lower_inp_list.count(i.lower())==1:
            return i
    return ""


print(first_non_repeating_letter('Go hang a salami, I\'m a lasagna hog!'))