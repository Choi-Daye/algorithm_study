def solution(arr, queries):
    for query in queries :
        s,e,k = query
        i = s
        while i <= e :
            if i % k == 0 :
                arr[i] += 1
            i += 1
    return arr