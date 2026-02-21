# стандартные системы счисления
# двоичная система
num = 20
print(bin(num)[2:]) # str
print(f'{num:b}')
# восьмеричная система
print(oct(num)[2:])
print(f'{num:o}')
# шестнадцатеричная система
print(hex(num)[2:])
print(f'{num:x}')

# перевод в 10 систему
# int(num,sys), где sys - система из которой переводим

# перевод в любую систему счисления ( 2 <= sys <= 9)
def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]

return res[::-1] if res else '0'

print(convert(20, 2))


# перевод в любую систему счисления ( 2 <= sys <= 36)
from string import printable
def convert(num, sys):
    res = ''
    while num:
        res += printable[num % sys]
        num //= sys
    return res[::-1]

return res[::-1] if res else '0'

# полезные алгоритмы
# сумма цифр двоичной системы
num_bin = '10101'
print(num_bin.count('1'))
# сумма цифр любой системы (2 <= sys <= 9)
print(sum(map(int, num_bin)))
# сумма цифр любой системы (2 <= sys <= 36)
print(sum(map(lambda x: int(x,36), num_bin)))


# замена символов в строке
# заменить N символов слева - R[N:]
# заменить n символов справа - R[:-N]
# заменить все символы в строке (все 0 поменять на 1)
R = '1010'
R = R.replace('0', '1')

# заменить все символы в строке (все 1 поменять на 3,а 3 поменять на 1)
R = R.replace('1','*')
R = R.replace('3','1')
R = R.replace('*','3')

# усложненные варианты вопросов
# максимальное N при максимальном R
ans.append([R,N])
print(max(ans))
# минимальное  N при минимальном R
ans.append([R,N])
print(min(ans))
# минимальное  N при максимальном R
ans.append([R,N])
ans = sorted(ans, key=lambda x:(-x[0], x[1]))
print(ans[0])
# максимальное N при минимальном R
ans.append([R,N])
ans = sorted(ans, key=lambda x:(-x[0], x[1]))
print(ans[0])




