from copy import copy

a = [1, 2, 3, 4, 5]
b = [i for i in a]

print(b)

b[0] = 99

print(b)
print(a)

c = copy(a)