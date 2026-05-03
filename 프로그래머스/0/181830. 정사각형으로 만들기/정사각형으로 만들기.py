def solution(arr):
    answer = []
    col = len(arr[0])   # 열
    row = len(arr)      # 행

    if col > row:   # 열 > 행
        for i in range(col-row):
            l = []
            for j in range(col):
                l.append(0)
            arr.append(l)
        return arr
    
    elif row > col: # 행 > 열
        for a in arr:
            for j in range(row-col):
                a.append(0)
            answer.append(a)
        return answer
    
    else:           # 행 = 열
        return arr