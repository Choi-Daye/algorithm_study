def solution(number, limit, power):
    answer, cnt = [], 0
    
    for num in range(1, number+1):
        for n in range(1, int(num**0.5) + 1):
            if num % n == 0:
                if n**2 == num:
                    cnt += 1
                else:
                    cnt += 2
                
        if cnt > limit:
            answer.append(power)
        else:
            answer.append(cnt)
        cnt = 0
    return sum(answer)