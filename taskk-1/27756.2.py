from itertools import permutations

graph = 'ah hb bf fg ge ea ac ch cf gd ed'.split()

matrix = '247 148 467 123 68 358 13 256'.split()

for i in permutations('ahbfgecd'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)

37 + 28 = 65