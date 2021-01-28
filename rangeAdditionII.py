def maxCount(m, n, ops):
    if len(ops) == 0: return m*n
    mins = [m, n]
    for i, j in ops:
        mins[0] = min(mins[0], i)
        mins[1] = min(mins[1], j)

    return mins[0]*mins[1]
