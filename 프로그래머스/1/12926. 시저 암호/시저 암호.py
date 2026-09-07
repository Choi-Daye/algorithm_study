def solution(s, n):
    answer = ''
    string = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
    
    for i in s:
        if i == ' ':
            answer += ' '
        elif i.isupper():
            idx = string.find(i.lower())
            answer += string[idx+n].upper()
        else:
            idx = string.find(i)
            answer += string[idx+n]
            
    return answer