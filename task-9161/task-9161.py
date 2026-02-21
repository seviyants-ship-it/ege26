from string import printable
def convert(num, sys):
    res = ''
    while num:
        res += printable[num % sys]
        num //= sys
    return res[::-1]
ans = []
for x in range(1,2024):
    num = convert(9**2024 + 9**1987 - x, 9)
    if num .count('8') == 1984:
        ans.append(x)
print(max(ans))
