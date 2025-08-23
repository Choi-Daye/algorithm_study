def solution(arr, flag):
    X = []
    for i, boolean in enumerate(flag) : 
        if boolean :
            X += [arr[i]] * (arr[i]*2)
        else :
            for j in range(arr[i]) :
                X.pop() 
    return X