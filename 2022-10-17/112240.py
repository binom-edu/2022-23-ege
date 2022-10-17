def getDivisors(x):
    i = 1
    ans = set()
    while i ** 2 <= x:
        if x % i == 0:
            ans.add(i)
            ans.add(x // i)
        i += 1
    return ans

def isPerfect(n):
    divisors = getDivisors(n)
    return sum(divisors) - n == n

n = int(input())
if isPerfect(n):
    print('YES')
else:
    print('NO')