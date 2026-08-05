def solution(polynomial):
    x, c = 0, 0
    answer = ''
    
    for p in polynomial.split(' + '):
        if 'x' in p:
            coef = p.replace('x','') or '1'
            x += int(coef)
        else:
            c += int(p)         
    
    if x == 1:
        answer += 'x'
    elif x > 1:
        answer += str(x)+'x'
    # else:
    #     continue
        
    if c > 0:
        if answer:
            answer += ' + '+str(c)
        else:
            answer += str(c)
        
    return answer