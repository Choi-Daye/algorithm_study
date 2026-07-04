def solution(my_string):
    answer = ""
    
    for s in my_string:
        if s.isdigit():
            answer += s
        else:
            answer += ' '

    return sum(int(n) for n in answer.split())
