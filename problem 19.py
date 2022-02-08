def solution(price, money):
    answer = 0  #?
    sum = 0
    for i in price:
        sum += i
    answer = money - sum
    if answer <0:
        answer = -1
    return answer

price = [2100, 3200, 2100, 800]
money = 10000
print(solution(price, money))