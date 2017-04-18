def multiplication_table(row,col):
    # Good Luck!
    return [[k * j for k in [i for i in range(1, col + 1)]] for j in range(1, row + 1)]

print multiplication_table(4,3)