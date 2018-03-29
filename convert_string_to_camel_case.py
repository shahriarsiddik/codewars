import re


def to_camel_case(text):
    if text == '':
        return ''
    txt_splt = re.split('; |, |\*|\n|-|_',text)
    camel_txt = ""
    if len(txt_splt) > 1:
        first = txt_splt[0]
        for i in txt_splt[1:]:
            camel_txt += i[0].upper()+i[1:]
        return first+camel_txt


print(to_camel_case("A-B-C"))
