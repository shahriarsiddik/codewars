import time
start_time = time.time()
from collections import Counter


# def find_arr2(arrA, arrB, rng, wanted):
#     if wanted=='even':
#         my_set = [i for i in list(set(arrA) & set(arrB)) if i >= rng[0] and i <= rng[1] and i%2==0]
#         return sorted([elem for elem in my_set if arrA.count(elem) > 1 and arrB.count(elem) > 1])
#     else:
#         my_set = [i for i in list(set(arrA) & set(arrB)) if i >= rng[0] and i <= rng[1] and i % 2 != 0]
#         return sorted([elem for elem in my_set if arrA.count(elem) > 1 and arrB.count(elem) > 1])


def find_arr(arrA, arrB, rng, wanted):
    my_list=[]

    my_set = [i for i in list(set(arrA) & set(arrB)) if i >= rng[0] and i <= rng[1] and i%2==0] if wanted=='even' else [i for i in list(set(arrA) & set(arrB)) if i >= rng[0] and i <= rng[1] and i%2!=0]

    inter1= Counter(arrA)
    inter2 = Counter(arrB)
    for i in my_set:
        if inter1[i]>1 and inter2[i]>1:
            my_list.append(i)
    return sorted(my_list)

# arrB = random.sample(range(-500,500),4)
rng = [-300, 500]
wanted = 'even'


print(find_arr([],[],rng,wanted))
# print find_arr2(arrA,arrB,rng,wanted)

print("time elapsed: {:.2f}s".format(time.time() - start_time))