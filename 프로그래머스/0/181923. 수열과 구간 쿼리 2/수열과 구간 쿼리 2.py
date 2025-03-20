def solution(arr, queries):
    answer = []
    l = []
    for s, e, k in queries :
        for i in arr[s:e+1] :   
            if i > k :    
                l.append(i)
        if not l :    
            l.append(-1)
        answer.append(min(l))
        l = []    
    return answer