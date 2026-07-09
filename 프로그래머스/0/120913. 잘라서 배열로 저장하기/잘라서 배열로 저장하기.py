def solution(my_str, n):
    answer = []
    i = 0
    
    while True:
        if i+n < len(my_str):
            answer.append(my_str[i:i+n])
        else:
            answer.append(my_str[i:])
            break
        i += n
        
    return answer