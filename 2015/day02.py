def load_packages():
    with open('day02_input') as f:
        for line in f.readlines():
            yield tuple( int(d) for d in line.strip().split('x') )


def paper_area(l, w, h):
    """
    >>> paper_area(2, 3, 4)
    58
    >>> paper_area(1, 1, 10)
    43
    """
    sides = [
        l*w,
        w*h,
        h*l,
    ]
    return sum(2*s for s in sides) + min(sides)


def ribbon_length(l, w, h):
    """
    >>> ribbon_length(2, 3, 4)
    34
    >>> ribbon_length(1, 1, 10)
    14
    """
    perimeters = [
        2*(l + w),
        2*(w + h),
        2*(h + l),
    ]
    volume = l * w * h
    return min(perimeters) + volume


if __name__ == '__main__':
    packages = list(load_packages())
    print(sum( paper_area(*p) for p in packages ))
    print(sum( ribbon_length(*p) for p in packages ))
