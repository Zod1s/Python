from random import randrange

data = [randrange(0, 100) for _ in range(400)]

def mergesort(a):
    if len(a) <= 1:
        return a
    else:
        mid = len(a)//2

        left = a[:mid]
        right = a[mid:]

        left = mergesort(left)
        right = mergesort(right)

        return merge(left, right)

def merge(a, b):
    merged = []
    while len(a) > 0 and len(b) > 0:
        if a[0] < b[0]:
            merged.append(a.pop(0))
        else:
            merged.append(b.pop(0))

    if len(a) > 0:
        merged.extend(a)
    elif len(b) > 0:
        merged.extend(b)

    return merged

sor = mergesort(data)
print(sor)