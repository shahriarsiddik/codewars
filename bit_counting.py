def countBits(n):
    return str(bin(int(n))).count('1')

print(countBits(10))
