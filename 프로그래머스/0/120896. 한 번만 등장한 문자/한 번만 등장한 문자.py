def solution(s):
    cnt_num = {}
    
    for i in s:
        if i in cnt_num:
            cnt_num[i] += 1
        else:
            cnt_num[i] = 1
    
    
    return ''.join(sorted(k for k in cnt_num if cnt_num[k] == 1))