def solution(arr, k):
    ret = []
    for a in arr:
        for b in a:
            ret.append(b)
    ret.sort()
    return ret[k-1]

arr = [[5, 12, 4, 31],
        [24, 13, 11, 2],
        [43, 44, 19, 26],
        [33, 65, 20, 21]]
k = 4
print(solution(arr, k))

