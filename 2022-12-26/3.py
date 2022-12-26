alf = '123456'
n = 0

def f(s):
    global n
    if len(s) == 5:
        if s.count('1') == 1:
            n += 1
        return
    for i in alf:
        f(s + i)

f('')
print(n)