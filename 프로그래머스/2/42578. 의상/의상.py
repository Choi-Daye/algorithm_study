def solution(clothes):
    hash = {}
    answer = 1
    
    for c in clothes:
        hash[c[1]] = hash.get(c[1], []) + [c[0]]
    
    for k in hash:
        answer *= len(hash.get(k))+1

    return answer - 1