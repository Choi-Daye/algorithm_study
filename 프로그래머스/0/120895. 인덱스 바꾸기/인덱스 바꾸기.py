def solution(my_string, num1, num2):
    a = min(num1, num2)
    b = max(num1, num2)
    return my_string[:a] + my_string[b] + my_string[a+1:b] + my_string[a] + my_string[b+1:] 