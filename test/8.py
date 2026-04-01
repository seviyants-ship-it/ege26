from itertools import product

alph = 'цитрус'
ans = []
for  pos, val in enumerate(product(alph,repeat=5),start=1):
    val =''.join(val)
    if val.count('и') == 2 and 'цц' not in val:
        ans.append(pos)
print(ans[-1])

ответ не тот