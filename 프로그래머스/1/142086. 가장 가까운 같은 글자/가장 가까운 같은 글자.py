def solution(s):
    pre = {}
    answer = []
    
    for i, w in enumerate(s):
        answer.append(i-pre[w]) if w in pre else answer.append(-1)
        pre[w] = i
        
    return answer