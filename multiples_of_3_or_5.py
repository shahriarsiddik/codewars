def solution(number):
    i=1
    sol_sum = 0
    while i<number:
        if i%3 ==0 or i%5==0:
            sol_sum+=i
        i+=1
    return sol_sum

print solution(10)