def solution(myString, pat):
    myString, pat = myString.lower(), pat.lower()
    if pat in myString :
        return 1
    else :
        return 0