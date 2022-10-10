a = [1, 2, 13, 17]

for i in a:
    if i % 2 != 0:
        i *= 2
    print(i)

print(a)

for i in range(len(a)):
    if a[i] % 2 != 0:
        a[i] *= 2
    print(a[i])

print(a)