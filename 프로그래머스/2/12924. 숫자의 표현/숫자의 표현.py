def solution(n):
    num = [i for i in range(n+1)]
    start, end = 1, 1
    answer = 0
    
    while start != n and end != n:
        if sum(num[start:end+1]) < n:
            end += 1
        elif sum(num[start:end+1]) > n:
            start += 1
        else:
            answer += 1
            start += 1
            
    return answer + 1