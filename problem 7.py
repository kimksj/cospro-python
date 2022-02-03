#7
def solution(scores):
    count = 0
    for s in scores:
        if 650 <= s and s < 800:
            count += 1
    return count

scores = [600, 900, 780, 660, 800, 600, 500, 720, 860, 700]
print(solution(scores))
