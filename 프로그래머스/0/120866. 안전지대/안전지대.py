def solution(board):
    tnt = []
    n = len(board)
    
    for i, row in enumerate(board):
        for j, col in enumerate(row):
            if col == 1:
                tnt.append([i,j])
    
    for r, c in tnt:
        for i in range(r - 1, r + 2):
            for j in range(c - 1, c + 2):
                if 0 <= i < n and 0 <= j < n:
                    board[i][j] = 1
    
    return sum(row.count(0) for row in board)
