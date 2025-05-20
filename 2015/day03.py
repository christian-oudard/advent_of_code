from collections import defaultdict

UP, DOWN, LEFT, RIGHT = '^v<>'


def deliver_instructions(houses, instructions):
    x, y = (0, 0)
    def deliver():
        houses[(x, y)] += 1

    deliver()
    for c in instructions:
        if c == UP:
            y += 1
        elif c == DOWN:
            y -= 1
        elif c == LEFT:
            x -= 1
        elif c == RIGHT:
            x += 1
        else:
            continue
        deliver()


def one_santa(instructions):
    """
    >>> one_santa('>')
    2
    >>> one_santa('^>v<')
    4
    >>> one_santa('^v^v^v^v^v')
    2
    """
    houses = defaultdict(int)
    deliver_instructions(houses, instructions)
    return len(houses.keys())


def two_santas(instructions):
    """
    >>> two_santas('^v')
    3
    >>> two_santas('^>v<')
    3
    >>> two_santas('^v^v^v^v^v')
    11
    """
    houses = defaultdict(int)
    a, b = unzip(instructions)
    deliver_instructions(houses, a)
    deliver_instructions(houses, b)
    return len(houses.keys())


def unzip(instructions):
    a = []
    b = []
    switch = True
    for c in instructions:
        if switch:
            a.append(c)
        else:
            b.append(c)
        switch = not switch
    return (a, b)


if __name__ == '__main__':
    with open('day03_input') as f:
        instructions = f.read()
    print(one_santa(instructions))
    print(two_santas(instructions))
