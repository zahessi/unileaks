# Задача: Дан числовой массив. Проверить, есть ли такие два числа в массиве, 
# перемножив которые мы получим заданное число X.

def find(arr, x):
    u = [e for e in arr for m in arr if e*m == x]
    return len([e for e in arr for m in arr if e*m == x]) >= 2

assert find([1, 2, 3], 17) == False
assert find([23, 4, 1, 3], 12) == True