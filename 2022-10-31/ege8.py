def to_oct(n):
    ans = ''
    while n > 0:
        d = n % 8
        ans = str(d) + ans
        n //= 8
    return ans

def f(n):
    n_oct = to_oct(n)
    if n_oct.count('6') != 1:
        return False
    evens = '1357'
    for i in evens:
        if i + '6' in n_oct or '6' + i in n_oct:
            return False
    return True

ans = 0
for i in range(8 ** 4, 8 ** 5):
    if f(i):
        ans += 1
print(ans)