def solution(n):
    answer = ''

    while n:
        answer += str(n%3)
        n //= 3
        
    return sum(3**i * int(num) for i, num in enumerate(answer[::-1]))