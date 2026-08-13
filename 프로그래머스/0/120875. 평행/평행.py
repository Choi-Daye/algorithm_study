def solution(dots):
    a_x, a_y = dots[0]
    b_x, b_y = dots[1]
    c_x, c_y = dots[2]
    d_x, d_y = dots[3]
    
    if (a_y-b_y) / (a_x-b_x) == (c_y-d_y) / (c_x-d_x):
        return 1
    if (a_y-c_y) / (a_x-c_x) == (b_y-d_y) / (b_x-d_x):
        return 1
    if (a_y-d_y) / (a_x-d_x) == (b_y-c_y) / (b_x-c_x):
        return 1
    
    return 0