def solution(num):
    cnt = 0
    
    while True:
        if cnt == 500:
            return -1
        elif num == 1:      # 2
            return cnt
        elif not num % 2: # 1-1
            num = num/2
        else:             # 1-2
            num = num * 3 + 1
        cnt += 1