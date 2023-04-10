import random
n =10
a = [random.randint(0, 10) for i in range(n)]
print(a)

a.sort(reverse=True)
print(a)