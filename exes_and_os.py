def xo(s):
    # print s.count('x')
    x_cnt = s.count('x')+s.count('X')
    o_cnt = s.count('o')+s.count('O')
    return True if x_cnt==o_cnt else False

print xo('xxoo')