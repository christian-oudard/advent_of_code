# text = '''\
# MMMSXXMASM
# MSAMXMSMSA
# AMXSXMAAMM
# MSAMASMSMX
# XMASAMXAMM
# XXAMMXXAMA
# SMSMSASXSS
# SAXAMASAAA
# MAMMMXMMMM
# MXMXAXMASX'''
text = open('day4_input').read()

grid = text.splitlines()
height = len(grid)
width = len(grid[0])
assert all( len(line) == width for line in grid )


def add(a, b):
    ax, ay = a
    bx, by = b
    return (ax + bx, ay + by)


def get(grid, p):
    if p is None:
        return ' '
    x, y = p
    if (
        0 <= x < width and
        0 <= y < height
    ):
        return grid[y][x]
    else:
        return ' '


# Part 1.
TARGET_WORD = 'XMAS'
total = 0
for y in range(height):
    for x in range(width):
        for direction in [
            (1, 0),
            (1, 1),
            (0, 1),
            (-1, 1),
            (-1, 0),
            (-1, -1),
            (0, -1),
            (1, -1),
        ]:
            p = (x, y)
            chars = []
            for i in range(len(TARGET_WORD)):
                chars.append(get(grid, p))
                p = add(p, direction)
            found = ''.join(chars)
            if found == TARGET_WORD:
                total += 1
print(total)


# Part 2.
TARGET_WORDS = ['MAS', 'SAM']
total = 0
for y in range(height):
    for x in range(width):
        center = (x, y)
        words = []
        for pattern in [
            [(1, 1), (0, 0), (-1, -1)],
            [(1, -1), (0, 0), (-1, 1)],
        ]:
            positions = [ add(center, d) for d in pattern ]
            chars = [ get(grid, p) for p in positions ]
            words.append(''.join(chars))
        if all( w in TARGET_WORDS for w in words ):
            total += 1
print(total)
