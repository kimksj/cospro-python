def soulution(data):
    total = sum(data)
    average = total / len(data)
    cnt = 0
    for d in data:
        if d <= average:
            cnt += 1
    return cnt

data= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(soulution(data))