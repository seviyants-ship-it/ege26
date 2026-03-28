from itertools import permutations

graph = 'дг бг бж же ев вд да ак гк бк ае ка'.split()
matrix = '248 137 268 15 467 357 256 13'.split()

print(*range(1,9))
for i in permutations('абвгдежк'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)

