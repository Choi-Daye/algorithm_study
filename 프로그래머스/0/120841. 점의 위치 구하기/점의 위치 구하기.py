def solution(dot):
    answer = 0
    
    # x좌표 : 음수
    if dot[0] < 0 :
        # y좌표 : 음수
        if dot[1] < 0 :
            answer = 3
        # y좌표 : 양수
        else :
            answer = 2
    # x좌표 : 양수        
    else :
        # y좌표 : 음수
        if dot[1] < 0 :
            answer = 4
        # y좌표 : 양수
        else :
            answer = 1
            
    return answer