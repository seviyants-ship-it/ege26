from string import printable
from itertools import product
cnt = 0
for  val in product('полина',repeat=8):
    val = ''.join(val)
    if sum(val.count(i) for i in 'плн') > sum(val.count(i) for i in 'оиа'):
        cnt += 1
print(cnt)