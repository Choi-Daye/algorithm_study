def solution(myString, pat):
    myString, pat = myString.lower(), pat.lower()
    return int(pat in myString)