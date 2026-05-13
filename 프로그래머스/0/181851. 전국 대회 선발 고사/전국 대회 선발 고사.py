def solution(rank, attendance):
    num = 1
    select = []

    while len(select) != 3:
        if attendance[rank.index(num)] == True:
            select.append(rank.index(num))
        num += 1
   
    return 10000*select[0] + 100*select[1] + select[2]