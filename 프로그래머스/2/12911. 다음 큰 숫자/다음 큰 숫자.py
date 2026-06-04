def solution(n):
    next_num = n + 1
    
    while (str(bin(n)[2:])).count("1") != (str(bin(next_num)[2:])).count("1"):
        next_num += 1
    
    return next_num