def solution(myStr):
    answer = []
    word =''
    
    for i, s in enumerate(myStr):
        if s not in ['a', 'b', 'c']:
            word += s
            if i == len(myStr)-1:
                answer.append(word)
        elif s in ['a', 'b', 'c']:
            if word:
                answer.append(word)
                word = ''
        
    return ["EMPTY"] if not word else answer