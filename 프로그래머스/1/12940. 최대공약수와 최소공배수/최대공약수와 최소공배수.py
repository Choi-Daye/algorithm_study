def solution(n, m):
    for i in range(min(n, m), 0, -1):
        if not (n % i or m % i):
            a = i
            break
    
    for j in range(m, n*m + 1):
        if not (j % n or j % m):
            b = j
            break
    
    return [a, b]