import dis

def f():
    x = 0
    for i in range(10):
        x += i
    return x

def g():
    x = 0
    i = 0
    while i < 10:
        x += i
        i += 1
    return x

assert f() == g()
print("dis f")
print(dis.dis(f))
print("")

print("dis g")
print(dis.dis(g))
print("")
