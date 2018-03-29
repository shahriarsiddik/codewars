
def divisors(integer):
    res = []
    for i in range(2,integer):
        if integer%i==0:
            res.append(i)
    if not res:
        return str(integer)+" is prime"
    else:
        return res


for j in range(100):
    print("for "+str(j)+" ---------> "+ str(divisors(j))+'\n')
