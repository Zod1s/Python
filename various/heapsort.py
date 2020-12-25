# from random import randrange

def heapify(a, len, index):
    ltson = 2 * index + 1
    rtson = 2 * index + 2
    largest = index

    if ltson < len and a[ltson] > a[largest]:
        largest = ltson

    if rtson < len and a[rtson] > a[largest]:
        largest = rtson
    
    if largest != index:
        a[index], a[largest] = a[largest], a[index]
        a = heapify(a, len, largest)
    return a    

def buildheap(a):
    for i in range((len(a)-1)//2, -1, -1):
        a = heapify(a, len(a), i)
    return a

def heapsort(a):
    buildheap(a)
    n = len(a)
    for i in range(n-1, -1, -1):
        a[0], a[i] = a[i], a[0]
        a = heapify(a, i, 0)
    return a

# data = [randrange(0, 100) for _ in range(40)]
# d = heapsort(data.copy())
# print(d)