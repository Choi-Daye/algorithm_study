def solution(lines):
    line = {}
    
    for s, f in lines:
        for n in range(s, f):
            line[n] = line.get(n, 0) + 1
                    
    return sum(1 for _, v in line.items() if v > 1)