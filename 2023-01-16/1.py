# функция разложения числа на множители

def getFactors(n):
    ans = []
    d = 2
    while d ** 2 <= n:
        while n % d == 0:
            ans.append(d)
            n //= d
        d += 1
    if n > 1:
        ans.append(n)
    return ans

print(getFactors(100))