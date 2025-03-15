def solution(numLog):
    answer = ""
    for i in range(1, len(numLog)) :
        cal = numLog[i] - numLog[i-1]
        if cal == 1 :
            answer += "w"
        elif cal == -1 :
            answer += "s"
        elif cal == 10 :
            answer += "d"
        else :
            answer += "a"
        
        if i == len(numLog)-1 :
            break
    return answer