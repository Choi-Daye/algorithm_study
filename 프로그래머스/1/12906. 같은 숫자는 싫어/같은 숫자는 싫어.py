def solution(arr):
    answer = []
    for i, a in enumerate(arr):
        if i == 0:
            answer.append(a)
        elif arr[i-1] != arr[i]:
            answer.append(a)
    return answer