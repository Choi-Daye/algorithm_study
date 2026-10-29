def solution(elements):
    answer = set(elements)
    l = len(elements)
    elements = elements*2
    
    for i in range(2, l+1):
        for j in range(0, l):
            if i == l:
                answer.add(sum(elements[:l]))
                break
            else:
                answer.add(sum(elements[j:j+i]))

    return len(answer)