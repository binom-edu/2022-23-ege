# напечатать двоичное представление числа n

def printBin(n):
    d = n % 2
    if n > 1:
        printBin(n // 2)
    print(d, end='')

printBin(13)