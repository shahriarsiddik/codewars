def last(i,*args):
    print type(i)
    if args:
        return args[-1]
    else:
        if type(i)==int:
            return i
        else:
            return i[-1]

print last(1)