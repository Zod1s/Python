def iterBinSearch(ls, t):
    low = 0
    high = len(ls)
    while low < high:
        mid = (low + high) // 2
        if ls[mid] == t:
            return mid
        elif ls[mid] < t:
            low = mid + 1
        else:
            high = mid
    return len(ls)

def recBinSearch(ls, t, low, high):
    if low > high:
        return len(ls)
    mid = (low + high) // 2
    if ls[mid] == t:
        return mid
    elif ls[mid] < t:
        return recBinSearch(ls, t, mid + 1, high)
    else:
        return recBinSearch(ls, t, low, mid - 1)

a = [1, 2, 3, 8, 10, 12, 22, 23, 24, 25]
b = 23
i = iterBinSearch(a, b)
# i = recBinSearch(a, b, 0, len(a))
print(f"Elem a[{i}] = {a[i]}, should be {b}")