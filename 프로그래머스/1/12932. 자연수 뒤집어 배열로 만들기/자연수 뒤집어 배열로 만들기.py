def solution(n):
    answer = []
    for n in str(n):
        answer.append(int(n))
    return answer[::-1]