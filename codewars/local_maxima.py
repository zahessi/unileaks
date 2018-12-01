def pick_peaks(a):
    final = {'pos': [], 'peaks': []}
    if not a or len(a) < 3: return final
    for i in range(1, len(a)-1):
        if a[i] >= a[i+1] and a[i] > a[i-1]:
            if not len(final['peaks']) or a[i] != final['peaks'][-1] or set(a[:i])>1:
                if len(set(a[i:])) > 1:
                    final['pos'].append(i)
                    final['peaks'].append(a[i])
    return final

a = pick_peaks( [1, 3, 3, 3, 3, 5, 13, 19, 8, 11, 15, 19, 16, -1, 4, 7, 1, -3, 1, 0, 5, 18, 2, 14, 19, -3, 20, 2, 13])
try:
    assert a == {'pos': [7, 11, 15, 18, 21, 24, 26], 'peaks': [19, 19, 7, 1, 18, 19, 20]}
except AssertionError:
    print(a)