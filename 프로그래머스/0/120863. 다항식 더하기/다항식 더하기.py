def solution(polynomial):
    x, c = 0, 0
    
    for p in polynomial.split():
        if p == '+':
            continue
        elif 'x' in p:
            if p == 'x':
                x += 1
            else:
                x += int(p[:-1])
        else:
            c += int(p)
                
    if x != 0 and c != 0:
        if x == 1:
            return 'x + ' + str(c)
        else:
            return str(x) + 'x + ' + str(c)
    elif x == 0:
        return str(c)
    elif c == 0:
        if x == 1:
            return 'x'
        else:
            return str(x) + 'x'