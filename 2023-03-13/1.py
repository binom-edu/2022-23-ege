def f(x, y, z, w):
    return (x <= int(not w)) and (y <= x) and z

print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if f(x, y, z, w):
                    print(x, y, z, w)