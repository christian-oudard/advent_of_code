import re

memory = open('day3_input').read()

# Part 1.
matches = re.finditer(r'mul\(([0-9]+),([0-9]+)\)', memory)
total = 0
for m in matches:
    a = int(m.group(1))
    b = int(m.group(2))
    total += a * b
print(total)

# Part 2.
matches = re.finditer(r"do\(\)|don't\(\)|mul\(([0-9]+),([0-9]+)\)", memory)
total = 0
do_flag = True
for m in matches:
    s = m.group(0)
    if s == "do()":
        do_flag = True
    elif s == "don't()":
        do_flag = False
    elif do_flag:
        a = int(m.group(1))
        b = int(m.group(2))
        total += a * b
print(total)
