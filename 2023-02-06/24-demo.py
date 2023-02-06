import sys
sys.stdin = open('24.txt')

s = input()

ans = 0
cnt = 0
for i in range(0, len(s) - 1, 2):
    if s[i] in 'CDF' and s[i + 1] in 'AO':
        cnt += 1
        ans = max(ans, cnt)
    else:
        cnt = 0
for i in range(1, len(s) - 1, 2):
    if s[i] in 'CDF' and s[i + 1] in 'AO':
        cnt += 1
        ans = max(ans, cnt)
    else:
        cnt = 0
print(ans)