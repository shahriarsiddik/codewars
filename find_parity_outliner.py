def find_outlier(integers):
	is_even = 0
	is_odd = 0
	for i in range(0,3):
		if integers[i]%2==0:
			is_even+=1
		else:
			is_odd+=1
	if is_even>is_odd:
		for j in integers:
			if j%2!=0:
				return j
	else:
		for j in integers:
			if j%2==0:
				return j



print find_prity([160, 3, 1719, 19, 11, 13, -21])