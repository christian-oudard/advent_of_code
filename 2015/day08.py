def parse(literal):
    """
    >>> parse('""')
    ''
    >>> parse('"abc"')
    'abc'
    >>> parse('"aaa\\"aaa"')
    'aaa"aaa'
    >>> parse('"\\x27"')
    "'"
    """
    if not (literal[0] == '"' and literal[-1] == '"'):
        raise ValueError('Not a string literal.')

    return ''.join(parse_iter(literal[1:-1]))


def parse_iter(s):
    s = iter(s)
    try:
        while True:
            c = next(s)
            if c == '\\':
                c2 = next(s)
                if c2 == '\\':
                    yield '\\'
                elif c2 == '"':
                    yield '"'
                elif c2 == 'x':
                    hex_code = next(s) + next(s)
                    yield chr(int(hex_code, 16))
                else:
                    raise ValueError(f'Invalid escape: {c}{c2}')
            else:
                yield c
    except StopIteration:
        return


def unparse(s):
    r"""
    >>> print(unparse('""'))
    "\"\""
    >>> print(unparse('"abc"'))
    "\"abc\""
    >>> print(unparse('"aaa\\"aaa"'))
    "\"aaa\\\"aaa\""
    >>> print(unparse('"\\x27"'))
    "\"\\x27\""
    """
    literal = ''.join(escape_iter(s))
    return f'"{literal}"'


def escape_iter(s):
    for c in s:
        if c in ['\\', '"']:
            yield '\\'
        yield c


if __name__ == '__main__':
    total_literal = 0
    total_in_memory = 0
    total_escaped = 0
    with open('day08_input') as f:
        for line in f.readlines():
            literal = line.strip()
            total_literal += len(literal)
            total_in_memory += len(parse(literal))
            total_escaped += len(unparse(literal))

    print(total_literal - total_in_memory)  # Part 1.
    print(total_escaped - total_literal)  # Part 2.

