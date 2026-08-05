def solution(quiz):
    answer = []
    
    for q in quiz:
        result = 0
        q_list = q.split()
        
        if q_list[1] == '+':
            result = int(q_list[0]) + int(q_list[2])
        else:
            result = int(q_list[0]) - int(q_list[2])

        answer.append('O' if result == int(q_list[-1]) else 'X')
    
    return answer