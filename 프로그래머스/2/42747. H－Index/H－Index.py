def solution(citations):
    answer = 0
    for h in range(0, len(citations)+1):
        higher = sum(1 for c in citations if c >= h)
        if higher < h:
            return answer
        else:
            answer = h
    return answer