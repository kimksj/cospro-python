def func_a(k):
    sum = 0
    for i in range(1, k + 1):
        sum += i
    return sum

def solution(n, m):
    sum_to_m = func_a(m)
    sum_to_n = func_a(n-1)
    answer = sum_to_m - sum_to_n
    return answer

n = 5
m = 10
print(solution(n, m))           #45