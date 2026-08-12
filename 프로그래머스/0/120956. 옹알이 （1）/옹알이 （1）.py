def solution(babbling):
    answer = 0
    speak = ["aya", "ye", "woo", "ma"]
    
    for b in babbling:
        while b:
            if b[:2] in speak:
                b = b[2:]
            elif b[:3] in speak:
                b = b[3:]
            else:
                break
        if not b:
            answer += 1
    
    return answer