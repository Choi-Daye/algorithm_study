def solution(s):
    answer, find_eng = '', ''
    eng = {'zero':0, 'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9}
    
    for e in s:
        if e.isdigit():
            answer += e
        else:
            find_eng += e
            if find_eng in eng:
                answer += str(eng[find_eng])
                find_eng = ''
                
    return int(answer)