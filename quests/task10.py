# Если элемент матрицы равен 0, то всю строку и весь столбец нужно обнулить.
def zero(arr):
    zeroes_pointers = []
    for i, m in enumerate(arr):         # строка
        for j, el in enumerate(m):      # столбец
            if el == 0: 
                zeroes_pointers.append((i, j))

    for i, j in zeroes_pointers:
        for ind, el in enumerate(arr[i]): arr[i][ind] = 0
        for k in arr: k[j] = 0
    return arr

    
assert zero([[1, 2, 3], [4, 5, 6], [7, 8, 0]]) == [[1, 2, 0],[4, 5, 0],[0, 0, 0]]