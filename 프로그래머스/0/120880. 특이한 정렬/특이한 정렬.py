def solution(numlist, n):
    answer = []
    
    dist = sorted([num - n for num in numlist])
    
    m_dist = [d for d in dist if d < 0]
    p_dist = [d for d in dist if d >= 0]
    
    while m_dist or p_dist:
        if not m_dist:
            answer.append(p_dist.pop(0) + n)
        elif not p_dist:
            answer.append(m_dist.pop() + n)
        else:
            if abs(m_dist[-1]) < p_dist[0]:
                answer.append(m_dist.pop() + n)
            else:
                answer.append(p_dist.pop(0) + n)
    
    return answer