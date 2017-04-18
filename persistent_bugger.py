def persistence(n):
    # your code
    n=list(str(n))
    count=0
    while len(n)>1:
        print reduce(lambda x, y: x * y, map(int, n))
        n=list(str(reduce(lambda x, y: x * y, map(int, n))))
        count+=1
    return count

# print persistence(39)