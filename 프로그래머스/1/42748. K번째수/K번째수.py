def solution(array, commands):
    answer = []
    
    for i, j, k in commands:
        cut = sorted(array[i-1:j])
        answer.append(cut[k-1])
    
    return answer