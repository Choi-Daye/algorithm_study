def solution(want, number, discount):
    dic = {}
    want_dic = dict(zip(want, number))
    cnt = 0
    
    for i, d in enumerate(discount):
        dic[d] = dic.get(d, 0) + 1
            
        if i >= 10:
            old_item = discount[i-10]
            dic[old_item] -= 1
            if dic[old_item] == 0:
                del dic[old_item]
        
        if want_dic == dic:
            cnt += 1
            
    return cnt