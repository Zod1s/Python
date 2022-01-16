def cripta(a, b, maiusc, char_spec):
    l = 26
    if not char_spec:
        n = a + b
        r = n // l
        c = n - (l * r)
        if maiusc:
            d = c + 65
        else:
            d = c + 97
    else:
        d = a
    c = chr(d)
    return c


def decripta(b, c, maiusc, char_spec):
    l = 26
    if not char_spec:
        n = c - b + 26
        r = n // l
        a = n - (l * r)
        if maiusc:
            d = a + 65
        else:
            d = a + 97
    else:
        d = c
    a = chr(d)
    return a
