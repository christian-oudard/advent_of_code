def all_sum_combinations(sizes, target):
    """
    >>> len(list(all_sum_combinations([20, 15, 10, 5, 5], 25)))
    4
    """
    for nums in all_combinations(sizes):
        if sum(nums) == target:
            yield nums


def all_combinations(items):
    for index in range(2**len(items)):
        yield select(items, index)


def select(items, index):
    """
    >>> select('abc', 0b101)
    ['a', 'c']
    """
    return  [
        items[i]
        for i in range(len(items))
        if index & 1<<i
    ]


if __name__ == '__main__':
    container_sizes = [
        int(line.strip())
        for line in open('day17_input').readlines()
    ]

    # Part 1.
    num_combinations = sum( 1 for _ in all_sum_combinations(container_sizes, 150) )
    print(num_combinations)

    # Part 2.
    smallest_combination = min(all_sum_combinations(container_sizes, 150), key=len)
    smallest_size = len(smallest_combination)
    small_combinations = filter(lambda c: len(c) == smallest_size, all_sum_combinations(container_sizes, 150))
    print(len(list(small_combinations)))
