f = open('10.txt', encoding='windows-1251')
s = f.read().split()
f.close()

cnt = 0
for i in s:
    if 'теперь' in i:
        cnt += 1
        print(i)

print(cnt)