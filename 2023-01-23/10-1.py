import re
s = open('10.txt', encoding='windows-1251').read()
ans = re.split('\W+', s).count('теперь')
print(ans)
