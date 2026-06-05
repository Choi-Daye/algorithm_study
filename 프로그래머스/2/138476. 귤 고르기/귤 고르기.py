def solution(k, tangerine):
    answer = 0
    tan_dic = {}
    
    for t in tangerine:
        if t in tan_dic:
            tan_dic[t] += 1
        else:
            tan_dic[t] = 1
        
    
    for i, n in enumerate(sorted(tan_dic.values(), reverse=True)):
        answer += n
        if answer >= k:
            return i+1
    