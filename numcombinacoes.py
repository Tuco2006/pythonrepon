def comb(m, n):
    if n == 0:
        return 1
    elif m == n:
        return 1
    elif m < n:
        return 0
    else:
        return comb(m - 1, n) + comb(m - 1, n - 1)

print(comb(3, 2))