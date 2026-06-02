def solution(sizes):
    h, w = [], []
    for s in sizes:
        h.append(max(s))
        w.append(min(s))
    return max(h) * max(w)