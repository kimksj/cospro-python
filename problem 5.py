def solution(arr):
    left, right = 0, len(arr)-1
    # left = 0, right = 3
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
          # 3            1            1            3
          # 1            4            4            1
        left += 1  #1 2 <- X
        right -= 1  #2 1 <- X
    return arr   #[1, 4, 1, 3]

arr = [3, 1, 4, 1]
print(solution(arr))