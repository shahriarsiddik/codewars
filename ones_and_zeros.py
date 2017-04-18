def binary_array_to_number(arr):
    num=''.join([str(i) for i in arr])
    return int(num,2)
print binary_array_to_number([0,1,1,1])