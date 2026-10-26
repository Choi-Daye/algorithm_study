def solution(n, arr1, arr2):
    answer, result = '', []
    
    for a, b in zip(arr1, arr2):
        num = str(int(bin(a)[2:]) + int(bin(b)[2:]))
        answer += ' '*(n-len(num))
        
        for c in num:
            if c == '0':
                answer += ' '
            else:
                answer += '#'
        
        result.append(answer)
        answer = ''
        
    return result