def solution(sides):
    answer = 0
    two_sum = 0
    
    # 가장 큰 값
    max_num = max(sides)
    # 가장 큰 값의 인덱스
    max_idx = sides.index(max_num)
    
    # max_idx가 아닌 두 수의 합
    for i in range(len(sides)) :
        if i != max_idx :
            two_sum += sides[i]
        else :
            pass
    
    # 삼각형의 가능성 여부 확인
    if two_sum > sides[max_idx] :
        answer = 1
    else :
        answer = 2
    
    return answer