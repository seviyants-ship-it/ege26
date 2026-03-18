from itertools import product, permutations

def f(x,y,w,z):
    return not (y <= (x == w)) and (z <= x)

for x1,x2,x3,x4,x5 in product([0,1],repeat=5):
    table = [
        (x1,1,1,x2,1),
        (0,x3,x4,0,1),
        (x5,0,1,0,1)
    ]
    if len(table) == len(set(table)):
        for p in permutations('xywz'):
            if all(f(**dict(zip(p,t))) == t[-1] for t in table):
                print(*p,sep='')