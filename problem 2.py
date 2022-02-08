def solution(price, grade):
    if grade == "S":
        price = price * 0.95
    elif grade == "G":
        price = price * 0.9
    elif grade == "V":
        price = price * 0.85
    return price

grade = "G"
price = 25000

print(solution(price, grade))
