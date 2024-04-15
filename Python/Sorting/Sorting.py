def bubbleSort(l):
    n = len(l)
    swapped = False
    for i in range(n-1):
        for j in range(n-i-1):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
                swapped = True
        if swapped == False:
            return l
    return l

def selectionSort(l):
    n = len(l)
    for i in range(n-1):
        min_ind = i
        for j in range(i+1,n):
            if l[j] < l[min_ind]:
                min_ind = j
        l[min_ind], l[i] = l[i], l[min_ind]
    return l


def InsertionSort(l):
    n = len(l)
    for i in range(1,n):
        x = l[i]
        j = i - 1
        while j >= 0 and x < l[j]:
            l[j+1] = l[j]
            j -= 1
        l[j+1] = x
    return l
        



l = [10 , 8, 20, 5]
print(InsertionSort(l))

#print(bubbleSort(l))