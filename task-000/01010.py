from itertools import product

ans = 0
alph='сентябрь'

for pos, val in enumerate(product(sorted(alph),repeat=5),start=1):
    val = ''.join(val)
    if pos % 2 == 0 and val[0] == 'р' and 'ь' not in val:
        ans = pos

print(ans)
