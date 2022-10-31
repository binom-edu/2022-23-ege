def r(n):
    nbin = bin(n)[2:]
    cnt = nbin.count('1')
    if cnt % 2 == 0:
        res = '10' + nbin[2:] + '0'
    else:
        res = '11' + nbin[2:] + '1'
    return int(res, 2)

n = 4
while r(n) <= 40:
    n += 1

print(n)
