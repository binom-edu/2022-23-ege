for i in range(1, 1000):
    s = i
    n = 50
    while s > 0:
        s //= 2
        n -= 3
    if n == 26:
        print(i)
        