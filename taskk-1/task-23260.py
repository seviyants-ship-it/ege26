from itertools import permutations

graph = 'ae ad dc cf fg ge hg ha hb bc bd' .split()
print(graph)
matrix = '346 348 12 127 678 15 458 257' .split()

for i in permutations('abcdefgh'):
    if all(str(i.find(x) + 1) in matrix[i.find(y)] for x , y in graph):
        print(*i)




from itertools import permutations

graph = 'AE AD DC CF FG GE HG HA HB BC BD'.split()
matrix = '346 348 12 127 678 15 458 257'.split()

print(*range(1, 9))
for i in permutations('ABCDEFGH'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)
