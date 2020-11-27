def fib(n):

    fib0 = 1
    fib1 = 1

    for i in range(1, n):
        # temp = fib1
        # fib1 += fib0
        # fib0 = temp

        fib0, fib1 = fib1, fib0 + fib1

    return fib1

print(fib(10))