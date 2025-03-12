def solution(code):
    answer = ''
    mode = 0
    
    for idx, i in enumerate(code) :
        # mode 0
        if mode == 0 :
            # change mode : 0 -> 1
            if i == "1" :
                mode = 1
                continue
            # only even
            if idx % 2 == 0 :
                answer += i
        # mode 1
        else :
            # change mode : 1 -> 0
            if i == "1" :
                mode = 0
                continue
            # only odd
            if idx % 2 == 1 :
                answer += i
    
    if answer :
        return answer
    else :
        return "EMPTY"