def solution(num1, num2):
    answer = -1
    if 0 < num1 and num2 <= 100 :
        answer = num1 % num2
    return answer