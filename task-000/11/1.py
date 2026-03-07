for n in range(1, 10 ** 6):
    L = 10 + 25
    i =ceil(log2(n))
    I = ceil(L * i / 8) + 48
    if 1536 * I <= 120 * 1024:
        print(N)