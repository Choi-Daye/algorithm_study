def solution(arr):
    num, cnt_num = [], {}
    answer = 1
    
    for a in arr:
        for i in range(2, a+1):
            if a == 1:
                num.append(1)
                break
            else:
                while a % i == 0:
                    num.append(i)
                    a //= i
        
        for n in set(num):
            if not cnt_num.get(n):
                cnt_num[n] = num.count(n)
            else:
                cnt_num[n] = max(cnt_num[n], num.count(n))
        
        num = []
        
    for d in cnt_num:
        answer *= (d ** cnt_num[d])

    return answer