def solution(n):
    answer = 0
    cnt = 1
    while cnt*2 <= n:
        answer += cnt * 2
        cnt += 1
    return answer