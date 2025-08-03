def solution(myString):
    answer = myString.split("x")   
    for i in answer :
            if "" in answer :
                answer.remove("") 
    answer.sort()
    return answer