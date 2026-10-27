import math

def solution(n):
    answer = 0
    
    for i in range(n):
        if n-2*i >= 0:
            answer += math.factorial(n-i) // (math.factorial(i) * math.factorial(n-i-i))
    
    return answer%1234567