def ackermann(m, n):
    if m == 0:
        return n + 1
    elif m > n and n == 0:
        return ackermann(m - 1, 1)
    else:
        return ackermann(m - 1, ackermann(m, n - 1))
