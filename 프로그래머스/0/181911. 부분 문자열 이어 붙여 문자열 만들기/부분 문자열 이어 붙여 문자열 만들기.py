def solution(my_strings, parts):
    answer = ''
    
    for word, (i, j) in zip(my_strings, parts) :
        answer += word[i:j+1]
    
    return answer