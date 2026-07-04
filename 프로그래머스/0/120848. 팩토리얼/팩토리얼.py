def solution(n):
    answer, cnt = 1, 1
    
    while answer <= n:
        cnt += 1
        answer *= cnt
        
    return cnt - 1