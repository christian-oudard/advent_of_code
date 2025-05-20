UP = '('
DOWN = ')'

with open('day01_input') as f:
    s = f.read()

# Part 1
level = 0
for c in s:
    if c == UP:
        level += 1
    elif c == DOWN:
        level -= 1
print(level)

# Part 2
level = 0
first_basement_position = None
for i, c in enumerate(s, start=1):
    if c == UP:
        level += 1
    elif c == DOWN:
        level -= 1
    if first_basement_position is None and level < 0:
        first_basement_position = i
print(first_basement_position)
