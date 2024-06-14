def solution(price):
    answer = 0
    
    if price < 100000 :
        answer = price
    elif price < 300000 :
        answer = price * (1 - 0.05)
    elif price < 500000 :
        answer = price * (1 - 0.1)
    else :
        answer = price * (1 - 0.2)
    return int(answer)