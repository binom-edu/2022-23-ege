# задача 15 демо
def f(x, a):
    return (int(x % 2 == 0) <= int(x % 3 != 0)) or (x + a >= 100)

for a in range(1, 1000):
    if all([f(x, a) for x in range(1, 1000)]):
        print(a)
        break