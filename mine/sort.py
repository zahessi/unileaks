arr = [3, 5, 2, 59, 12, 74, 0]

def bubble_sort(arr):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swapped = True
    return arr    

print(bubble_sort(arr))