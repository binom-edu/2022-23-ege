def f(x, y):
    k1, b1 = 1 / (3 ** 0.5), 0
    k2, b2 = -1 / (3 ** 0.5), 10
    return (x > 0) and (y > k1 * x + b1) and (y < k2 * x + b2)

ans = 0
for x in range(11):
    for y in range(11):
        if f(x, y):
            ans += 1
print(ans)