def solution(n):
    answer, cnt = [0,1], 2
    
    while cnt != n:
        answer.append(answer[cnt-1] + answer[cnt-2])    
        cnt += 1
    
    return (answer[n-1] + answer[n-2]) % 1234567