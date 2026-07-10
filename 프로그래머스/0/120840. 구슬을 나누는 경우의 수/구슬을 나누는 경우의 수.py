def solution(balls, share):
    answer, division, cnt = 1, 1, 0
    
    for i in range(balls, 0, -1):
        cnt += 1
        answer *= i
        division *= cnt
        
        if cnt == share:
            break
    
    return answer/division