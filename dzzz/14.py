from string import printable
def convert(num, sys):
    res = ''
    while num:
        res += printable[num % sys]
        num //= sys
    return res[::-1]

num = 432x3**15 + 86x86**15
print(convert(num,15).count(num))