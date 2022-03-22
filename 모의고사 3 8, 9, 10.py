#8
def solution(password, key):
    answer = 0
    match_cnt = 0
    for k in key:
        for p in password:
            if k == p:
                match_cnt += 1
                break
    if match_cnt >= len(key):
        answer = 1
    return answer


#9
def solution(scores):
    result = [0, 0, 0, 0]
    for i in range(4):
        for k in range(4):
            if i != k:
                result[i] += (scores[i][k] * 2)
    return result

scores = [['X', 1, 0, 0],
          [0, 'X', 0, 1],
          [1, 1, 'X', 1],
          [1, 0, 0, 'X']]
print(solution(scores))


#10
def solution(strings):
    result = 0
    for s in strings:
        length = len(s)
        result += (length / 4)
        if length % 4 > 0:
            result += 1
    return result

strings = [['a','b','c','d','e','f',1,2,3,4,5,6,7],
           ['r','s','e','f','a','q','w','t','d'],
           ['k','i','j','u']]

print(solution(strings))