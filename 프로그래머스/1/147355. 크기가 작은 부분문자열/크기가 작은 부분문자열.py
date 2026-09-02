def solution(t, p):
    return sum(1 for i in range(len(t)-len(p)+1) if int(t[i : len(p)+i]) <= int(p))