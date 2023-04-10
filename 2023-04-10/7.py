import sys
sys.stdin = open('26.txt')

n = int(input())
a = []
for i in range(n):
    a.append(int(input()))

a.sort(reverse=True)
b = [a.pop(0)]
while a:
    box = a.pop(0)
    if b[-1] - box >= 3:
        b.append(box)

print(len(b), b[-1])