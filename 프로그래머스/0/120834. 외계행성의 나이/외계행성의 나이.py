def solution(age):
    apb = ['a','b','c','d','e','f','g','h','i','j']
    return ''.join(apb[int(a)] for a in str(age))