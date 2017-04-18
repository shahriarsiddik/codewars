def multi(l_st):
    return reduce(lambda x,y:x*y,l_st)
def add(l_st):
    return reduce(lambda x,y:x+y,l_st)
def reverse(string):
    return string[::-1]


print multi([8,2,5])
print add([7,8,6,5,4,9])

print reverse("Hello World")