def columnZero(A):
    i = 0
    j = 0
    n = len(A)
    while i < n and j < n:
        if A[i][j] == 0:
            i += 1
        else:
            j += 1
            i = 0
    return j if j < n else -1

A = [
    [0, 1, 0],
    [0, 0, 0],
    [0, 0, 1]
]

print(columnZero(A))
