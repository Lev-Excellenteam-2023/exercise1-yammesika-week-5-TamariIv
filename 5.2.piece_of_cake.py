

def get_recipe_price(prices, optionals=[], **ingredients):      # from 5.2
    total = 0
    for name, amount in ingredients.items():
        if name in optionals:
            continue
        total += amount * (prices[name] / 100)
    return int(total)


if __name__ == '__main__':
    print(get_recipe_price({'chocolate': 18, 'milk': 8}, optionals=['milk'], chocolate=300))
    print(get_recipe_price({'chocolate': 18, 'milk': 8}, chocolate=200, milk=100))
    print(get_recipe_price({}))
