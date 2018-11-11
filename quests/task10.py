# Если элемент матрицы равен 0, то всю строку и весь столбец нужно обнулить.
def zero(arr):
    zero_count = arr.count(0)
    zeroes_pointers = []
    for i, m in enumerate(arr):         # строка
        for j, el in enumerate(m):      # столбец
            if el == 0: 
                zeroes_pointers.append((i, j))
                zero_count -= 1
        if not zero_count: break

    for i, j in zeroes_pointers:
        for ind, el in enumerate(arr[i]): arr[i][ind] = 0
        for k in arr: k[j] = 0
    return arr

    
for x in zero([[0, 2, 3], [4, 0, 6], [7, 8, 0]]):
    print(*x, sep=" ")