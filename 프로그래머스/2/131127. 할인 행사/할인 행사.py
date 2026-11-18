def solution(want, number, discount):
    want_dic, dic = {}, {}
    cnt = 0
    
    for w, n in zip(want, number):
        want_dic[w] = n
    
    for i, d in enumerate(discount):
        if d in dic:
            dic[d] += 1
        else:
            dic[d] = 1
            
        if i > 9:
            dic[discount[i-10]] -= 1
            if dic[discount[i-10]] == 0:
                dic.pop(discount[i-10])
        
        if want_dic == dic:
            cnt += 1
    return cnt