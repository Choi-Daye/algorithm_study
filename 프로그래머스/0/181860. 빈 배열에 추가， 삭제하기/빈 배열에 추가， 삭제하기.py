def solution(arr, flag):
    X = []
    for i, b in zip(arr, flag) : 
        if b :
            X.extend([i] * (i*2))
        else :
            for j in range(i) :
                X.pop() 
    return X