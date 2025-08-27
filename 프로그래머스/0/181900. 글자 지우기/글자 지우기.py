def solution(my_string, indices):
    indices.sort(reverse=True)
    list_string = list(my_string)
    
    for i in indices :
        list_string.pop(i)
        
    return ''.join(list_string)