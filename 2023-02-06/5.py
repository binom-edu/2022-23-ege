import sys
sys.stdin = open('a.txt', 'r')
sys.stdout = open('b.txt', 'w')

s = input()
print(s)
