
def group_by(func, iterable):       # from 6.5
    res_dict = {}
    for elem in iterable:
        key = func(elem)
        if key not in res_dict.keys():
            res_dict[key] = []
        res_dict[key].append(elem)
    return res_dict


if __name__ == '__main__':
    print(group_by(len, ["hi", "bye", "yo", "try"]))