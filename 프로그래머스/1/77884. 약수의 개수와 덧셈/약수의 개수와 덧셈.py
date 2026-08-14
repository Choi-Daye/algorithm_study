def divisor(n):
    num = set()
    for i in range(1, int(n**0.5)+1):
        if not n % i:
            num.add(i)
            num.add(n//i)
    return len(num)

def solution(left, right):
    answer = 0
    
    for i in range(left, right+1):
        if divisor(i) % 2:
            answer -= i
        else:
            answer += i

    return answer

