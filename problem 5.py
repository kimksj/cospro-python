#5
def solution(arr):
    left, right = 0, len(arr) -1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr

arr = [3,2, 4, 1]
print(solution(arr))
