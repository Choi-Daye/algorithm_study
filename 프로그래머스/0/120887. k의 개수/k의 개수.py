def solution(i, j, k):
    cnt = []
    
    for n in range(i, j+1):
        for s in str(n):
            cnt.append(s)
    
    return cnt.count(str(k))