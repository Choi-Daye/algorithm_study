def solution(s):
    cnt, cnt_0 = 0, 0
    
    while s != "1":
        cnt_0 += len(s)
        s = s.replace('0', '')
        cnt_0 -= len(s)
        s = bin(len(s))[2:]
        cnt += 1
    
    return [cnt, cnt_0]