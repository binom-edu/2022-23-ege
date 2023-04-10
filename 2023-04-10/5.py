import sys
sys.stdin = open('ex1.txt')

n = int(input())
a = []
for i in range(n):
    a.append(int(input()))

a.sort(reverse=True)
print(*a[:10], *a[-10:][::-1])
