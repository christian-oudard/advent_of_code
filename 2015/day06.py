from collections import namedtuple
from enum import StrEnum

SIZE = 1000

Rect = namedtuple('Rect' ,'x_left x_right y_top y_bottom')

class Action(StrEnum):
    ON = 'turn on'
    OFF = 'turn off'
    TOGGLE = 'toggle'


def rect_points(rect):
    for x in range(rect.x_left, rect.x_right + 1):
        for y in range(rect.y_top, rect.y_bottom + 1):
            yield (x, y)


def parse_line(line):
    """
    >>> parse_line('toggle 461,550 through 564,900')
    (<Action.TOGGLE: 'toggle'>, Rect(x_left=461, x_right=564, y_top=550, y_bottom=900))
    """
    line = line.strip()
    action = None
    remainder = None
    for action in Action.__members__.values():
        prefix = action + ' '
        if line.startswith(prefix):
            remainder = line[len(prefix):]
            break
    if action is None:
        raise ValueError('No action found')

    upper_left, lower_right = remainder.split(' through ', 2)
    x_left, y_top = upper_left.split(',')
    x_right, y_bottom = lower_right.split(',')
    rect = Rect(
        int(x_left),
        int(x_right),
        int(y_top),
        int(y_bottom),
    )
    return action, rect


def get_input():
    with open('day06_input') as f:
        for line in f.readlines():
            action, rect = parse_line(line)
            yield action, rect




def part_1():
    grid = {}
    for x in range(SIZE):
        for y in range(SIZE):
            grid[(x, y)] = False

    # Run instructions.
    for action, rect in get_input():
        for point in rect_points(rect):
            if action == Action.ON:
                grid[point] = True
            elif action == Action.OFF:
                grid[point] = False
            elif action == Action.TOGGLE:
                grid[point] = not grid[point]

    # Count lights that are turned on.
    total = 0
    for x in range(SIZE):
        for y in range(SIZE):
            if grid[(x, y)]:
                total += 1
    print(total)


def part_2():
    grid = {}
    for x in range(SIZE):
        for y in range(SIZE):
            grid[(x, y)] = 0

    # Run instructions.
    for action, rect in get_input():
        for point in rect_points(rect):
            if action == Action.ON:
                grid[point] += 1
            elif action == Action.OFF:
                if grid[point] > 0:
                    grid[point] -= 1
            elif action == Action.TOGGLE:
                grid[point] += 2

    # Count total brightness.
    total = 0
    for x in range(SIZE):
        for y in range(SIZE):
            total += grid[(x, y)]
    print(total)


if __name__ == '__main__':
    part_1()
    part_2()
