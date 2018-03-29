def fake_bin(x):
    return ''.join(['1' if i>5 else '0' for i in map(int, str(x))][:])


print(fake_bin(45385593107843568))