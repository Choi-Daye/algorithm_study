def solution(arr):
    cnt = 0
    ex_arr = []
    
    while True:
        cnt += 1
        ex_arr = arr.copy()
        
        for i, n in enumerate(arr):
            if n >= 50 and n % 2 == 0:
                n /= 2
                arr[i] = int(n)
            elif n < 50 and n % 2 == 1:
                n = (n*2 + 1)
                arr[i] = int(n)
                
        if ex_arr == arr:
            break
            
    return cnt - 1