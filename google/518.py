from functools import cache


def fibonacciSequence(start=0):
    maxLong = 1 << 64
    a, b = 0, 1
    for _ in range(start):
        a, b = b, a + b
    yield a
    yield b
    while True:
        c = a + b
        assert c < maxLong, "long integer overflow: " + str(c)
        yield c
        a, b = b, c


iterator = fibonacciSequence(5)
for _ in range(10):
    print(next(iterator))
