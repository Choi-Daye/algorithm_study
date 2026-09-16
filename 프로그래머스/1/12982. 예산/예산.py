def solution(d, budget):
    answer = sum(d)
    d.sort()

    while answer > budget:
        answer -= d.pop()
        
    return len(d)