def gcd(a, b):
    if a > b:
        x, y = a, b
    else:
        x, y = b, a

    while x % y != 0:
        x, y = y, x % y
    return y

