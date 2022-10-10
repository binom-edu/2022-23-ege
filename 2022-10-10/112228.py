# Вывести все простые числа в диапазоне

def isPrime(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

a, b = map(int, input().split())
success = False
for i in range(a, b + 1):
    if isPrime(i):
        success = True
        print(i, end=' ')

if not success:
    print(0)