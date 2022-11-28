# напечатать числа от 1 до n

def f(n):
    if n > 1:
        f(n - 1)
    print(n)

f(10)