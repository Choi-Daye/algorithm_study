def solution(board):
    list_1 = []
    answer = 0
    
    for i, b in enumerate(board):
        for j, n in enumerate(b):
            if n == 1:
                list_1.append([i,j])
    
    n = len(board)
    
    for l in list_1:
        a, b = l
    
        for i in range(a-1,a+2):
            if i < 0 or i >= n:
                continue
            for j in range(b-1, b+2):
                if j < 0 or j >= n:
                    continue
                board[i][j] = 1

    for b in board:
        answer += b.count(0)
    
    return answer