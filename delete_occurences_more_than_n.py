def delete_nth(order,max_e):
    i=0
    fin_list = []
    occ_dict = {}

    for element in order:
        if element not in occ_dict.keys():
            occ_dict[element]=1
            fin_list.append(element)
        else:
            if max_e<=occ_dict[element]:
                occ_dict[element] += 1
                fin_list.append(element)


    return fin_list

print delete_nth ([20,37,20,21],2)

