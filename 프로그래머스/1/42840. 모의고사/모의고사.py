def solution(answers):
    person_1 = [1,2,3,4,5] * 2000
    person_2 = [2,1,2,3,2,4,2,5] * 1250
    person_3 = [3,3,1,1,2,2,4,4,5,5] * 1000
    score, answer = [0, 0, 0], []
    
    for i, a in enumerate(answers):
        if person_1[i] == a:
            score[0] += 1
        if person_2[i] == a:
            score[1] += 1
        if person_3[i] == a:
            score[2] += 1
    
    for i, s in enumerate(score):
        if s == max(score):
            answer.append(i+1)
    
    return sorted(answer)