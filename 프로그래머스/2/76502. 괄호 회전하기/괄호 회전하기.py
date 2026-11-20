def solution(s):
    if len(s) % 2 == 1:
        return 0
    
    answer = 0
    item_dic = {']':'[', '}':'{', ')':'('}
    
    for i in range(len(s)):
        s_next = s[i:] + s[:i]
        items = []
        
        for item in s_next:
            if item in item_dic:
                if not items or items.pop() != item_dic[item]:
                    items.append(item)
                    break
            else:
                items.append(item)
                
        if not items:
            answer += 1
            
    return answer