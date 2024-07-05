def solution(str1, str2):
    for i in range(len(str1) - len(str2) + 1) :
        if str2 == str1[i:i+len(str2)] :
            return 1
            
    return 2