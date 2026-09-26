def solution(strings, n):
    n_string = {}
    answer = []
    
    for s in strings:
        if s[n] in n_string:
            n_string[s[n]].append(s)
        else:
            n_string[s[n]] = [s]
    
    for n in sorted(n_string.keys()):
        n_string[n].sort()
        answer += n_string[n]
    
    return answer