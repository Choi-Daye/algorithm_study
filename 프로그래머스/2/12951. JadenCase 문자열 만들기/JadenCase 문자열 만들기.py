def solution(s):
    return ' '.join([i[0].upper() + i[1:] if i else i for i in s.lower().split(' ')])