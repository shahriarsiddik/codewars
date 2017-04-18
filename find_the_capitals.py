def capitals(word):
    i=0
    res_list = []

    while i<len(word):
        if word[i].isupper():
            res_list.append(i)
        i+=1

    return res_list

print capitals('CodEWaRs')