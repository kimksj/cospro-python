#18
def solution(name_list):
    answer = 0
    for name in name_list:
        for n in name:
            if n == 'j' or n == 'k':
                answer += 1
                break
    return answer
name_list = ['james', 'sumin', 'jack', 'minsu']
print(solution(name_list))