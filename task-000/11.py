from math import log2, ceil

for N in range(1,100-000):
    L = 105
    i = ceil(log2(n))
    I = ceil(L * i / 8)
    if 65_536 * I >= 7 * 2 ** 20:
        print(N)
        break