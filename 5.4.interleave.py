
# Got help from chatGPT using the query "how to implement zip"
def interleave(*iterables):     # from 5.4
    res = []
    max_len = 0
    for iterable in iterables:
        length = len(iterable)
        if length > max_len:
            max_len = length

    iterators = [iter(it) for it in iterables]
    for i in range(max_len):
        items = [item for it in iterators if (item := next(it, None)) is not None]
        res += items
    return res


def gen_interleave(*iterables):     # from 5.4
    max_len = 0
    for iterable in iterables:
        length = len(iterable)
        if length > max_len:
            max_len = length

    iterators = [iter(it) for it in iterables]
    for i in range(max_len):
        items = [item for it in iterators if (item := next(it, None)) is not None]
        yield from items


if __name__ == '__main__':
    print(interleave('abc', [1, 2, 3], ('!', '@', '#')))
    print(interleave('a', [1, 2, 3], ('!', '@'), ('X', 'Y', 'Z')))
    print(list(gen_interleave('abc', [1, 2, 3], ('!', '@', '#'))))
