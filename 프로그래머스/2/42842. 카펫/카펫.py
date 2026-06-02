def solution(brown, yellow):
    for n in range(1, yellow+1):
        if yellow % n == 0:
            m = yellow // n
            if brown == 2*(m+n+2):
                return [m+2, n+2]