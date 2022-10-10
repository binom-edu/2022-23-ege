import random

n = int(input())

if n == 1:
    print(1)
    exit()
a = [1, 1]

for i in range(n - 2):
    a.append(a[-1] + a[-2])

print(*a)