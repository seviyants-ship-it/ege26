from itertools import product, permutations

def f(x,y,w,z):
    return not(y <= x) or (z <= w) or not z

for x1,x2,x3,x4,x5,x6,x7 in product([0,1],repeat=7):
    table = [
        (x1,0,x2,x3,0),
        (0,1,x4,x5,0),
        (1,x6,x7,0,0)
    ]
    if len(table) == len(set(table)):
        for p in permutations('xywz'):
            if all(f(**dict(zip(p,t))) == t[-1] for t in table):
                print(*p,sep='')