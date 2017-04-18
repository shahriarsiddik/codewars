from itertools import product

def possibilities(param):
    rpt = param.count('?')
    res = []
    for j in [i for i in product([0,1],repeat=rpt)]:
        res.append(param.replace('?','%s')%j)
    return res
print possibilities('101?')