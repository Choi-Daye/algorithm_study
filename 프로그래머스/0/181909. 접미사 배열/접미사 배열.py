def solution(my_string):
    answer = []
    i = 0
    
    for i in range(len(my_string)) :
        answer.append(my_string[i:])
        i += 1  
    answer.sort()
    
    return answer