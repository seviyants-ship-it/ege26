def convert(num,sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]
ans = []
for x in range(2,2026):
    num = convert(5**2025 + 5**200 - x,5)
    ans.append([x, num.count('4')])

print(ans)
print(max(ans))