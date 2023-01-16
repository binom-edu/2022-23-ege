# функция поиска делителей

def getDivisors(n):
    ans = [1, n]
    d = 2
    while d ** 2 <= n:
        if n % d == 0:
            ans.append(d)
            if n // d != d:
                ans.append(n // d)
        d += 1
    return ans

print(getDivisors(100))