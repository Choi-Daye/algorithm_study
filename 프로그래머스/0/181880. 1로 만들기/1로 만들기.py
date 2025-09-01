def solution(num_list):
    answer = 0
    for i in num_list :
        while i != 1 :
            answer += 1
            i //= 2
    return answer