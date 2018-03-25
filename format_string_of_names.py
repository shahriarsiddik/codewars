def namelist(name):
    res = ""
    is_first = True
    count = 0
    for i in name:
        count+=1
        if is_first:
            res+=i['name']
            is_first =False
        else:
            res += " & "+i['name'] if count==len(name) else ", "+i['name']
    return res
print(namelist([{'name':'Bart'},{'name':'Lisa'}]))