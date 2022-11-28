def f(start, x):
    if x == start:
        return 1
    if x < start:
        return 0
    if x == 17:
        return 0
    if x % 2 == 0:
        return f(start, x // 2) + f(start, x - 1)
    return f(start, x - 1)

print(f(1, 10) * f(10, 35))