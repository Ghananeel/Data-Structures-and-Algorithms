def mergeLists(a, b):
    m = len(a)
    n = len(b)
    i, j = 0, 0
    res = []
    while i < m and j < n:
        if (a[i] < b[j]):
            res.append(a[i])
            i += 1
        else:
            res.append(b[j])
            j += 1

    while i < m:
        res.append(a[i])
        i = i + 1

    while j < n:
        res.append(b[j])
        j = j + 1

    return res

a = [10, 15]
b = [5, 6, 6, 30, 40]

print(mergeLists(a,b))