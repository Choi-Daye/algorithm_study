def solution(a, b, c, d):
    answer, p, q = 1, 0, 0
    dice = [a, b, c, d]
    set_dice = set(dice)
    two_list = []

    # 네 가지
    if len(set_dice) == 1:
        answer = 1111 * list(set_dice)[0]
        
    elif len(set_dice) == 2:
        for d in list(set_dice):
            # 세 가지, 한 가지
            if dice.count(d) == 3:
                p = d
            elif dice.count(d) == 1:
                q = d
            # 두 가지, 두 가지
            else:
                two_list.append(d)
        if p and q:        
            answer = (10*p + q)**2
        else:
            answer = (max(two_list) + min(two_list)) * (max(two_list) - min(two_list))
        
    # 두 가지, 한 가지, 한 가지
    elif len(set_dice) == 3:
        for d in list(set_dice):
            if dice.count(d) == 1:
                answer *= d
                
    # 한 가지, 한 가지, 한 가지, 한 가지
    else:
        answer = min(list(set_dice))
                 
    return answer