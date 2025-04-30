from itertools import pairwise


def get_input():
    with open('day2_input') as f:
        for line in f.readlines():
            nums = [ int(n) for n in line.split() ]
            yield nums


def are_nums_safe(nums):
    diffs = [ b - a for a, b in pairwise(nums) ]
    # Numbers are strictly increasing or decreasing.
    if not (
        all( d > 0 for d in diffs ) or
        all( d < 0 for d in diffs )
    ):
        return False

    # Differences are between 1 and 3.
    if not all( 1 <= abs(d) <= 3 for d in diffs ):
        return False

    return True


# Part 1.
total = 0
for nums in get_input():
    if are_nums_safe(nums):
        total += 1
print(total)


# Part 2.
total = 0
for nums in get_input():
    # Try all possible removals, including nothing removed.
    num_sets = [nums]
    for i in range(len(nums)):
        new_nums = list(nums)
        del new_nums[i]
        num_sets.append(new_nums)
    for num_set in num_sets:
        if are_nums_safe(num_set):
            total += 1
            break
print(total)
