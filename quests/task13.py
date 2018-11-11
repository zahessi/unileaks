# Задача: Написать функцию, ктр "сжимает" строку. Если полученная строка 
# оказалась больше исходной, то вывести исходную.

# Например, дана строка "ZZZABBEEE", получить строку вида "Z3A1B2E3", т.е. 
# подставить счетчик вхождения символа.

def compress(s):
    c = {k:s.count(k) for k in s}
    new = []
    for k, v in c.items():
        new.extend([k, str(v)])
    new = ''.join(new)
    return s if len(new) > len(s) else new

assert compress('ZZZABBEEE') == 'Z3A1B2E3'
assert compress('abcca') == 'abcca'