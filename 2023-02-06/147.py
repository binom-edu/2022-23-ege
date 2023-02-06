import sys
sys.stdin = open('24-s2-1.txt')

s = input()
lst = []
for i in range(len(s) - 1):
    if s[i] == 'A':
        lst.append(s[i + 1])
    
alf = 'ABCDEFGHIJKLMNOPQRTUVWXYZ'
cnt = 0
for c in alf:
    x = lst.count(c)
    if x > cnt:
        cnt = x
        sym = c
print(sym, cnt)