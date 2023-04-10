import random
n =10
a = [random.randint(-100, 100) for i in range(n)]
print(a)

a.sort(key=lambda x: abs(x) % 10)
print(a)