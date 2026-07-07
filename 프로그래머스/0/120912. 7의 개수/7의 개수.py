def solution(array):
    return sum(str(n).count('7') for n in array)