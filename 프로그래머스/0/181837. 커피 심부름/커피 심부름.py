def solution(order):
    answer = 0
    
    for m in order:
        if "latte" in m:
            answer += 5000
        else:
            answer += 4500
    return answer