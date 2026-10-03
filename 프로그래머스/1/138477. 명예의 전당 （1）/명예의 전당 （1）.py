def solution(k, score):
    top, answer = [], []
    
    for s in score:
        top.append(s)
        top.sort()
        if len(top) > k:
            top = top[1:]
        answer.append(top[0])
    return answer