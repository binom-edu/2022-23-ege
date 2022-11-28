def f(x, n):
    if x == n:
        return 1
    if x > n:
        return 0
    if x == 17:
        return 0
    return f(x * 2, n) + f(x + 1, n)

print(f(1, 10) * f(10, 35))