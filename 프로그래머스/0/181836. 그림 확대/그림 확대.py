def solution(picture, k):
    answer = []

    for pic in picture:
        l = ''
        for p in pic:
            for i in range(k):
                l += p
        for j in range(k):
            answer.append(l)
    return answer