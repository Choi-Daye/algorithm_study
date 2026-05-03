def solution(arr, k):
    answer = []
    cnt = 0

    for a in arr:
        if a in answer:
            continue
        else:
            answer.append(a)
            if len(answer) >= k:
                break
    while len(answer) < k:
        answer.append(-1)
    return answer