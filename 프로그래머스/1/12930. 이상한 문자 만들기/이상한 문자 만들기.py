def solution(s):
    answer = ''
    
    for s in s.split(' '):
        for i, w in enumerate(s):
            if i % 2:
                answer += w.lower()
            else:
                answer += w.upper()
        answer += ' '
        
    return answer[:-1]