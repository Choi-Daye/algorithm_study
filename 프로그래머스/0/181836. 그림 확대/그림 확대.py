def solution(picture, k):
    answer = []
    for pic in picture:
        answer += [pic.replace('.', '.'*k).replace('x', 'x'*k)]*k
    return answer
