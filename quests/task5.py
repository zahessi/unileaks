# Написать функцию, ктр будет проверять можно ли преобразовать строку так,
# чтобы она стала палиндромом.

def just_palindrom(s):
    s = ''.join(filter(lambda x: x if str.isalnum(x) else None, s))
    return s == s[::-1]

def possible_palindrom(s):
    one = False
    s = [x for x in sorted(s) if x.isalnum()]
    for i in s:
        if s.count(i) == 1 and not one: 
            one = True
        elif s.count(i) % 2 and one:
            return False
    return True

assert possible_palindrom("саша") == True
assert possible_palindrom('а роза упала на лапу азора') == True