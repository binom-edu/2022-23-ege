# Алгоритм вычисления значения функции F(n), где n – натуральное число,
# задан следующими соотношениями:
# F(n) = 1 при n = 1;
# F(n) = n × F(n − 1), если n > 1.
# Чему равно значение выражения F(2023) / F(2020)?

import sys
sys.setrecursionlimit(3000)

def f(n):
    if n == 1:
        return 1
    return n * f(n - 1)

# print(f(2023) // f(2020))
for i in range(1, 6):
    print(i, f(i))