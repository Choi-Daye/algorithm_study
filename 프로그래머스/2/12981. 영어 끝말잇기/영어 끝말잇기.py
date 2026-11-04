def solution(n, words):
    answer = set()
    
    for i, word in enumerate(words):
        if i == 0:
            answer.add(word)
            continue
        
        if words[i-1][-1] != words[i][0]:
            return [i%n + 1, i//n + 1]
        else:
            ex_length = len(answer)
            answer.add(word)
            if ex_length == len(answer):
                return [i%n + 1, i//n + 1]
    
    return [0,0]