def solution(n):
    answer = ''
    for j in sorted([i for i in str(n)], reverse=True):
        answer += j
    return int(answer)