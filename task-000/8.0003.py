from itertools import permutations
cnt = 0
for val in set(permutations('парижанка')):
    val = ''.join(val)
    if val.count('аа') + val.count('аи') + val.count('иа') == 1 and 'aaa' not in val:
        cnt += 1
print(cnt)