# Вывести первый уникальный символ в строке

def first_unique(s):
    counted = {symb: s.count(symb) for symb in s}
    uni = [k for k, v in counted.items() if v == 1]
    return uni[0] if len(uni) else None

print(first_unique('asdgg1sda'))