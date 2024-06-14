def solution(array):
    array.sort()
    
    # 중앙값의 인덱스 찾기
    i = len(array) // 2
    answer = array[i]
    
    return answer