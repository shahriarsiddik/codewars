def one_two_three(n):
    if not n:
        return [0,0]
    res1 = ''
    m=n
    while m>9:
        res1 += '9'
        m-=9
    res1+=str(m)
    return [int(res1),int(''.join([str(1) for i in range(n)]))]


print(one_two_three(0))