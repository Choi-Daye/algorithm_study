def solution(s):
    answer = 0
    item_dic = {']':'[', '}':'{', ')':'('}
    
    for i in range(len(s)):
        s_next = s[i:] + s[:i]
        cnt = 0
        items = []
        
        for item in s_next:
            if not items:
                if item in [']', '}', ')']:
                    break

            if item in item_dic.keys():
                if items.pop() != item_dic[item]:
                    break
            else:
                items.append(item)
                
            cnt += 1
            
        if cnt == len(s) and not items :
            answer += 1
            
    return answer