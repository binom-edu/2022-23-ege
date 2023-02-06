ans = 0

with open('24-s1.txt') as fin:
    a = fin.read().splitlines()

for line in a:
    if line.count('K') > line.count('U'):
        ans += 1
print(ans)