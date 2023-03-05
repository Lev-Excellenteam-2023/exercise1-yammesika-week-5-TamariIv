

def join(*args, sep='-'):       # from 5.2
    if not args:
        return None
    res = []
    for l in args:
        res += l
        res += sep
    res = res[:-1]
    return res


if __name__ == '__main__':
    print(join([1, 2], [8], [9, 5, 6], sep='@'))
    print(join([1, 2], [8], [9, 5, 6]))
    print(join([1]))
    print(join())
