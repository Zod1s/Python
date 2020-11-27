def search(e, a):
    if e not in a:
        return False
    else:
        start = 0
        end = len(a) - 1
        found = False
        while (end >= start):
            middle = (start + end) // 2
            if a[middle] == e:
                return middle
            elif a[middle] < e:
                start = middle + 1
            else:
                end = middle - 1

#se voglio farlo ricorsivo, devo passargli anche gli estremi