def solution(x1, x2, x3, x4):
    X = True if x1 or x2 else False
    Y = True if x3 or x4 else False
    answer = True if X and Y else False
    return answer