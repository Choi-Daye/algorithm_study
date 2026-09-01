def solution(n, m):
    for i in range(min(n, m)):
        if not (n % (i+1) or m % (i+1)):
            a = i+1
    
    for j in range(m, n*m + 1):
        if not (j % n or j % m):
            b = j
            break
    
    return [a, b]