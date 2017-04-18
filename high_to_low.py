def high_and_low(number):
    first_elem = int(number.split()[0])
    res = [first_elem,first_elem]
    for r in number.split():
        r = int(r)
        if r>res[0]:
            res[0] = r
        if r<res[1]:
            res[1] = r

    return str(res[0])+" "+str(res[1])

print high_and_low("-1 -1 0")