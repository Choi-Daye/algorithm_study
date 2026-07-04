def solution(array, n):
    min_num = 100
    answer = 0
    
    for i in array:
        if abs(n - i) < min_num:
            min_num = abs(n - i)
            answer = i
        elif abs(n - i) == min_num:
            answer = min(answer, i)
        else:
            continue
    
    return answer