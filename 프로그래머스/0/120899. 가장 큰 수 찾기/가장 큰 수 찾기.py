def solution(array):
    answer = []
    max, cnt = 0, 0
    
    for i in array : 
        if i > max :
            max = i
            # max 인덱스 번호
            idx = cnt
        # 인덱스 번호
        cnt += 1
            
    answer.append(max)
    answer.append(idx)
    
    return answer