def solution(arr):
    answer = []
    
    for i in arr :
        if i >= 50 :
            if i % 2 == 0 :
                answer.append(i / 2)
            else :
                answer.append(i)
        else :
            if i % 2 != 0 :
                answer.append(i * 2)
            else :
                answer.append(i)
    return answer