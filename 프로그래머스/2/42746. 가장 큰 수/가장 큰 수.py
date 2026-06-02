def solution(numbers):
    num_list = []
    for num in numbers:
        num_list.append(str(num))
        
    num_list.sort(key=lambda x: x*3, reverse=True)
    
    answer = ''.join(num_list)
    
    # 예외처리
    if answer[0] == '0':
        return '0'
    
    return answer