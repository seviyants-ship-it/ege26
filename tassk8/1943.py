from itertools import product

alph = 'зеркало'

cnt = 0
for val in product(alph, repeat=6):
    val = ''.join(val)
    if 0 < val.count('к') <=4 and all(val.count(i) <= 1 for i in 'зерало'):
        cnt +=1
print(cnt)  
