from itertools import product
ans = []
alph='школа'

for pos, val in enumerate(product(alph,repeat=5),start=1):
    val = ''.join(val)
    if val == 'шалаш':
        ans.append(pos)
        print(ans)

не верно
