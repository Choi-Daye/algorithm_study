def solution(n):
    answer = 0
    
    # 짝수
    if n % 2 == 0 :
        for num in range(2, n+1, 2) :
            answer += num*num
    # 홀수
    else :
        for num in range(1, n+1, 2) :
            answer += num
    return answer