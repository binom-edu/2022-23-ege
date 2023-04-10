import sys
sys.stdin = open('ex2.txt')

n = int(input())
a = []
for i in range(n):
    x, y = map(int, input().split())
    a.append([x, y])

a.sort(key=lambda x: [x[0], -x[1]])
print(a[:10], a[-10:])