import random
alf = 'ABC'

n = 10 ** 6
with open('24-s2.txt', 'w') as fout:
    for i in range(n):
        fout.write(random.choice(alf))
