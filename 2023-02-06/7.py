import sys
sys.stdin = open('24-s2.txt')

s = input()
ans = 1
while 'C' * ans in s:
    ans += 1

print(ans - 1)