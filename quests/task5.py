# Написать функцию, ктр будет проверять можно ли преобразовать строку так,
# чтобы она стала палиндромом.


def just_palindrom(s):
    s = ''.join(filter(lambda x: x if str.isalnum(x) else None, s))
    return s == s[::-1]

assert just_palindrom("101") == True
assert just_palindrom('а роза упала на лапу азора') == True