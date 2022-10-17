def f(lst: list):
    mx = mn = lst[0]
    s = 0
    for i in lst:
        s += i
        if i > mx:
            mx = i
        if i < mn:
            mn = i
    return [mn, mx, (s - mx - mn) / 3]

a = [int(i) for i in input().split()]

res = f(a)
print(res[0], res[1])
print(res[2])