def solution(name, yearning, photo):
    answer = []
    num = 0
    
    for p in photo:
        answer.append(sum(yearning[i] for i, n in enumerate(name) if n in p))
        num = 0
    return answer