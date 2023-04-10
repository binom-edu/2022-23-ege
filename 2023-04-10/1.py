import random
n =10
a = [random.randint(0, 10) for i in range(n)]
print(a)

b = sorted(a)
print('a:', a)
print('b:', b)

a.sort()
print('Применили метод sort()')
print(a)