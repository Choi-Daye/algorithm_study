def solution(arr, queries):
    for s,e,k in queries :
        i = s
        while i <= e :
            if i % k == 0 :
                arr[i] += 1
            i += 1
    return arr