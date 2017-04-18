def get_sum(a,b):
    if a==b:
        return a
    else:
        if a>b:
            a,b=b,a
        return sum([i for i in range(a,b+1)])
print get_sum(-1, 0)