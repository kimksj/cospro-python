#16
def solution(height, k):
    answer = 0
    n = len(height)  #안씀
    for h in height:
        if h > k:
            answer += 1
    return answer

height = [165, 170, 175, 180, 184]
k = 175
print(solution(height, k))