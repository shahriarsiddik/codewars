def shifted_diff(first, second):
    if first== second:
        return 0
    else:
        for i in range(1,len(first)):
            if first[-i:]+first[:-i]==second:
                return i

    # code here!


print(shifted_diff("isn't", "'tisn"))
