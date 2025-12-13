def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()
    
    reserve_only = []
    lost_only = []
    
    # 두 개 가지고 와서 하나 도난 당한 사람 제외
    for r in reserve :
        if r not in lost :
            reserve_only.append(r)
    for l in lost :
        if l not in reserve :
            lost_only.append(l)

    # 앞 -> 뒤 순으로 체육복 빌려주기
    for r in reserve_only :
        if r-1 in lost_only :
            lost_only.remove(r-1)
        elif r+1 in lost_only :
            lost_only.remove(r+1)

    return n - len(lost_only)
