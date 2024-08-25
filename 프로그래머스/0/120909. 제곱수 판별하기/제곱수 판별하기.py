def solution(n):
    num = 1
    
    while True :
        number = num * num
        num += 1
        
        if number == n :
            answer = 1
            break
        else : 
            if number > n :
                answer = 2
                break
        
    return answer