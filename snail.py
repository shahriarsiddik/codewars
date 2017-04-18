def snail(array):
    mod_list = []
    fin_list = []
    if len(array) == 1:
        return array[0]
    if len(array)>1 and len(array[0])==1:
        for i in array:
            fin_list.append(i[0])
        return fin_list
    while array:
        rem_list = []
        left_col = []
        right_col = []
        for i in array[1:len(array)-1]:
            right_col.append(i[-1])
            left_col.insert(0,i[0])
            if len(i)>1:
                rem_list.append(i[1:-1])
            else:
                rem_list=[]
        mod_list.append(array[0])
        mod_list.append(right_col)
        mod_list.append(array[-1][::-1])
        mod_list.append(left_col)
        if len(rem_list)==1:
            mod_list.append(rem_list[0])
            rem_list=[]
        array = rem_list
    for j in mod_list:
        for k in j:
            fin_list.append(k)
    return fin_list
print snail([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]])
# res: [1, 2, 3, 4, 5, 10, 15, 20, 25, 24, 23, 22, 21, 16, 11, 6, 7, 8, 9, 14, 19, 18, 17, 12, 13]
# print snail([[1, 2, 3, 4, 5]])
# print snail([[1],[2],[3]])
#=> [1,2,3,6,9,8,7,4,5]

# print snail([[1,2,3],[4,5,6],[7,8,9]])