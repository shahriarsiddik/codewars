def delete_nth(order,max_e):
    fin_list = []
    for i in order:
        if fin_list.count(i)<max_e:
            fin_list.append(i)
    return fin_list

print delete_nth ([1,1,3,3,7,2,2,2,2],3)
