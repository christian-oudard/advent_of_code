from collections import defaultdict
from functools import reduce
from operator import mul
from itertools import combinations_with_replacement, pairwise


def parse_ingredient(line):
    """
    >>> parse_ingredient('Sprinkles: capacity 2, durability 0, flavor -2, texture 0, calories 3\\n')
    {'name': 'Sprinkles', 'capacity': '2', 'durability': '0', 'flavor': '-2', 'texture': '0', 'calories': '3'}
    """
    name, prop_str = line.strip().split(': ')
    ingr = {'name': name}
    for prop in prop_str.split(', '):
        key, value = prop.split()
        ingr[key] = int(value)
    return ingr


def load_data(filename):
    with open(filename) as f:
        return [
            parse_ingredient(line)
            for line in f.readlines()
        ]


def score(ingredients, mixture):
    """
    >>> ingredients = [
    ... {'name': 'Butterscotch', 'capacity': -1, 'durability': -2, 'flavor': 6, 'texture': 3, 'calories': 8},
    ... {'name': 'Cinnamon', 'capacity': 2, 'durability': 3, 'flavor': -2, 'texture': -1, 'calories': 3},
    ... ]
    >>> score(ingredients, (44, 56))
    62842880
    """
    ingredient_scores = []
    for prop in ['capacity', 'durability', 'flavor', 'texture']:
        ingredient_scores.append(
            sum(
                ingr[prop] * amount
                for ingr, amount in zip(ingredients, mixture)
            )
        )
    if any( s <= 0 for s in ingredient_scores ):
        return 0
    return product(ingredient_scores)


def calories(ingredients, mixture):
    return sum(
        ingr['calories'] * amount
        for ingr, amount in zip(ingredients, mixture)
    )


def product(iterable):
    return reduce(mul, iterable)


def optimal_mixture(ingredients, total_amount=100, target_calories=None):
    """
    >>> ingredients = [
    ... {'name': 'Butterscotch', 'capacity': -1, 'durability': -2, 'flavor': 6, 'texture': 3, 'calories': 8},
    ... {'name': 'Cinnamon', 'capacity': 2, 'durability': 3, 'flavor': -2, 'texture': -1, 'calories': 3},
    ... ]
    >>> optimal_mixture(ingredients)
    ((44, 56), 62842880)
    """
    best_mixture = None
    best_score = 0
    for mixture in numbers_with_sum(total_amount, len(ingredients)):
        s = score(ingredients, mixture)
        c = calories(ingredients, mixture)
        if target_calories is not None and c != target_calories:
            continue
        if s > best_score:
            best_mixture = mixture
            best_score = s
    return best_mixture, best_score


def numbers_with_sum(total, count):
    """
    Generate all combinations of `count` numbers which sum to `total`.
    >>> list(numbers_with_sum(3, 3))
    [(0, 0, 3), (0, 1, 2), (0, 2, 1), (0, 3, 0), (1, 0, 2), (1, 1, 1), (1, 2, 0), (2, 0, 1), (2, 1, 0), (3, 0, 0)]
    """
    for bars in combinations_with_replacement(range(total + 1), count - 1):
        bars = (0,) + bars + (total,)
        yield tuple( hi - lo for lo, hi in pairwise(bars) )


if __name__ == '__main__':
     ingredients = load_data('day15_input')
     print(optimal_mixture(ingredients))
     print(optimal_mixture(ingredients, target_calories=500))
