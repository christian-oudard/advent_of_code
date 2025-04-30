from collections import defaultdict

left = []
right = []
with open('day1_input') as f:
    for line in f.readlines():
        l, r = ( int(n) for n in line.split() )
        left.append(l)
        right.append(r)

# Part 1.
left.sort()
right.sort()
total = 0
for l, r in zip(left, right):
    total += abs(l - r)
print(total)

# Part 2.
right_counts = defaultdict(int)
for r in right:
    right_counts[r] += 1
total = 0
for l in left:
    total += l * right_counts[l]
print(total)
