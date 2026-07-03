def solution(num, k):
    return list(str(num)).index(str(k))+1 if str(num).count(str(k)) else -1