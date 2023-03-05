import random
from datetime import datetime, timedelta
import os


def the_way(path):      # from 5.1
    res = []
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        if os.path.isfile(file_path):
            file_name = os.path.basename(file_path)
            if file_name.startswith("deep"):
                res.append(file_name)
    return res


def no_vinaigrette():       # from 5.1
    date1 = input("Enter the first date in format YYYY-MM-DD:")
    date2 = input("Enter the second date in format YYYY-MM-DD:")
    date1 = datetime.strptime(date1, '%Y-%m-%d').date()
    date2 = datetime.strptime(date2, '%Y-%m-%d').date()
    if date1 > date2:
        date1, date2 = date2, date1
    diff = date2 - date1

    rand_days = random.randrange(diff.days)
    rand_date = date1 + timedelta(days=rand_days)
    print(rand_date)
    if rand_date.weekday() == 0:
        print("I have no vinaigrette!")


def join(*args, sep='-'):       # from 5.2
    if not args:
        return None
    res = []
    for l in args:
        res += l
        res += sep
    res = res[:-1]
    return res


def get_recipe_price(prices, optionals=[], **ingredients):      # from 5.2
    total = 0
    for name, amount in ingredients.items():
        if name in optionals:
            continue
        total += amount * (prices[name] / 100)
    return int(total)


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


def group_by(func, iterable):       # from 6.5
    res_dict = {}
    for elem in iterable:
        key = func(elem)
        if key not in res_dict.keys():
            res_dict[key] = []
        res_dict[key].append(elem)
    return res_dict


if __name__ == '__main__':
    print(the_way('C:/Users/tamar/excellenteam/stuff'))
    no_vinaigrette()
    print(join([1, 2], [8], [9, 5, 6], sep='@'))
    print(get_recipe_price({'chocolate': 18, 'milk': 8}, optionals=['milk'], chocolate=300))
    print(list(interleave('a', [1, 2, 3], ('!', '@'), ('X', 'Y', 'Z'))))
    print(list(gen_interleave('a', [1, 2, 3], ('!', '@'), ('X', 'Y', 'Z'))))
    print(group_by(len, ["hi", "bye", "yo", "try"]))


