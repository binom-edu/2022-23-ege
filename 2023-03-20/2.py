def f(x, l, r):
    return int((5 <= x <= 30) == (14 <= x <= 23)) <= int(not (l <= x <= r))

ans = 0
for l in range(100):
    for r in range(l, 100):
        if all([f(x, l, r) for x in range(1000)]):
            ans = max(ans, r - l)
print(ans)