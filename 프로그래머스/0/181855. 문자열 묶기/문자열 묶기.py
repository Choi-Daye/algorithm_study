def solution(strArr):
    str_len = []
    num_max = 0
    
    for i in strArr:
        str_len.append(len(i))  
    for j in list(set(str_len)):
        if num_max <= str_len.count(j):
            num_max = str_len.count(j)

    return num_max