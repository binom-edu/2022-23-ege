import random

a, b, n = map(int, input().split())

lst = [random.randint(a, b) for i in range(n)]

evens = odds = 0
for i in lst:
    if i % 2 == 0:
        evens += 1
    else:
        odds += 1

print(*lst)
print(evens, odds)