for n in range(1,100_000):
    r = f'{n:b}'
    if r.count('1') % 2 == 0:
