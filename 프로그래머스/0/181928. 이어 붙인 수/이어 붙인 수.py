def solution(num_list):
    odd = ""
    even = ""
    answer = 0
    for i in num_list :
        if i % 2 :
            even += str(i)
        else :
            odd += str(i)
    return int(even) + int(odd)