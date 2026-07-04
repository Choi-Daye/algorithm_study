def solution(my_string):
    answer = 0
    num = ''
    for i, s in enumerate(my_string):
        if s in ['1','2','3','4','5','6','7','8','9','0']:
            num += s
            if i == len(my_string)-1:
                answer += int(num)
        else:
            try:
                answer += int(num)
                num = ''
            except Exception:
                continue
    return answer