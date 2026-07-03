def solution(my_string):
    answer = []
    
    return sorted([int(num) for num in my_string if num in ['0','1','2','3','4','5','6','7','8','9']])