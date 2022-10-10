def f(x):
    return [x, x ** 2, x ** 3]

for i in range(5):
    print(*f(i))