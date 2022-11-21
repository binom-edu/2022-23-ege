with open('22.csv') as fin:
    a = [[0, [0]]]
    for line in fin.readlines():
        line1 = line.split('#')
        buf = [int(line1[0]), [int(i) for i in line1[1].split('; ')]]
        a.append(buf)

ans = [0] * len(a)
for i in range(len(a)):
    proc = a[i]
    d = proc[0]
    dep = proc[1]
    start = 0
    for j in dep:
        start = max(start, ans[j])
    ans[i] = start + d
print(max(ans))
