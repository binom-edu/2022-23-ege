import random
n =10
a = [random.randint(-100, 100) for i in range(n)]
print(a)

def f(x):
    return abs(x) % 10

a.sort(key=f)
print(a)