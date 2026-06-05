def solution(n):
    cnt = 0
    answer = 1
    start, end = 1, 1
    
    while end <= n:
        if answer < n:
            end += 1
            answer += end
        elif answer > n:
            answer -= start
            start += 1
        else:
            cnt += 1
            answer -= start
            start += 1
    
    return cnt