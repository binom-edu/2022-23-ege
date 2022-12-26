import itertools
s = 'abcd'

for i in itertools.permutations(s):
    print(''.join(i))