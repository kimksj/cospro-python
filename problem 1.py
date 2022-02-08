def solution(shirt_size):
    re = [0 for _ in range(6)]

    for size in shirt_size:
        if size == "XS":
            re[0] += 1
        elif size == "S":
            re[1] += 1
        elif size == "M":
            re[2] += 1
        elif size == "L":
            re[3] += 1
        elif size == "XL":
            re[4] += 1
        elif size == "XXL":
            re[5] += 1

    print(re)

# TEST
shirt_size = ["XS", "S", "L", "L", "XL", "S"]
solution(shirt_size)