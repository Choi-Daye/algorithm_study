def solution(arr):
    num = 0
    
    while len(arr) > 2**num:
        num += 1
        
    for i in range(2**num - len(arr)):
        arr.append(0)
        
    return arr