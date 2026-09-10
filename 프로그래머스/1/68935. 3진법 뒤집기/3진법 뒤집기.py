def solution(n):
    answer = ''

    while n >= 3:
        answer += str(n%3)
        n //= 3
        
    answer += str(n)
    return sum(3**i * int(num) for i, num in enumerate(answer[::-1]))