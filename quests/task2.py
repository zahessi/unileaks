def number(arr):
    for i in range(len(arr)):
        if i not in arr: return False
    return True

assert number([0, 1, 2, 3]) == True
assert number([4, 2, 0, 3]) == False