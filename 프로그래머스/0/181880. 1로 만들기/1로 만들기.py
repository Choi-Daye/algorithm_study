def solution(num_list):
    answer = 0
    for i in num_list :
        cnt = 0
        while i != 1 :
            cnt += 1
            i = i//2
        answer += cnt
    return answer