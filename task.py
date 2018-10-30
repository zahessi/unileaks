def unique(st):
    if not st: return False
    for i, e in enumerate(st):
        if e in st[i+1:]: return False
    return True

assert unique('aa') == False
assert unique('abadkjsld') == False
assert unique('aa') == False
assert unique('fsl') == True