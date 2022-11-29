
def halton(b):
    """Generator function for Halton sequence."""
    n, d = 0, 1
    while True:
        x = d - n
        if x == 1:
            n = 1
            d *= b
        else:
            y = d // b
            while x <= y:
                y //= b
            n = (b + 1) * y - x
        yield n / d



if __name__ == '__main__':
    n = 256
    f = open("output.txt", "a")
    iterable = halton(3)
    i = 0
    for it in iterable:
        if i < n:
            f.write(it)
            if (i < n - 1):
                f.write(',\n')
            i += 1
        else:
            break
    f.close()
