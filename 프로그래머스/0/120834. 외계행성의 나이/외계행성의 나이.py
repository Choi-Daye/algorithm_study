def solution(age):
    apb = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    return ''.join(apb[int(a)] for a in str(age))