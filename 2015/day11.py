from collections import deque
from itertools import islice, pairwise


def main():
    s = open('day11_input').read().strip()
    s = next_valid_password(s)
    print(s)
    s = next_valid_password(s)
    print(s)


def next_valid_password(s):
    """
    >>> next_valid_password('abcdefgh')
    'abcdffaa'
    >>> next_valid_password('ghijklmn')
    'ghjaabcc'
    """
    while True:
        s = increment(s)
        if is_valid(s):
            return s


def increment(s):
    """
    >>> increment('xx')
    'xy'
    >>> increment('xy')
    'xz'
    >>> increment('xz')
    'ya'
    >>> increment('ya')
    'yb'
    >>> increment('zzz')
    'aaa'
    """
    s = list(s)
    i = len(s) - 1
    while i >= 0:
        s[i], carry = incr_char(s[i])
        if carry == 0:
            break
        else:
            i -= 1
    return ''.join(s)


CHAR0 = ord('a')
NUM_CHARS = 26

def incr_char(c):
    """
    >>> incr_char('j')
    ('k', 0)
    >>> incr_char('z')
    ('a', 1)
    """
    n = ord(c) - CHAR0
    n = (n + 1)
    carry = 0
    if n >= NUM_CHARS:
        carry = 1
        n -= NUM_CHARS
    c_incr = chr(CHAR0 + n)
    return c_incr, carry


def is_valid(s):
    return all((
        has_increasing_straight(s),
        no_confusing_letters(s),
        has_doubled_letters(s),
    ))


def has_increasing_straight(s, n=3):
    """
    >>> has_increasing_straight('hijklmmn')
    True
    >>> has_increasing_straight('abbceffg')
    False
    """
    for window in sliding_window(s, n):
        if is_straight(window):
            return True
    return False


def is_straight(s):
    for a, b in pairwise(s):
        maybe_b, carry = incr_char(a)
        if carry == 1:
            return False
        if maybe_b != b:
            return False
    return True


def sliding_window(iterable, n):
    iterator = iter(iterable)
    window = deque(islice(iterator, n - 1), maxlen=n)
    for x in iterator:
        window.append(x)
        yield tuple(window)


CONFUSING_LETTERS = 'iol'

def no_confusing_letters(s):
    return not any( c in s for c in CONFUSING_LETTERS )


def has_doubled_letters(s, n=2):
    """
    >>> has_doubled_letters('aabcc', n=2)
    True
    >>> has_doubled_letters('aabaa', n=2)
    False
    >>> has_doubled_letters('abbbc', n=2)
    False
    """
    doubled_letters = set()
    count = 0
    previous_was_double = False
    for a, b in pairwise(s):
        if not previous_was_double:
            if a == b:
                if a not in doubled_letters:
                    count += 1
                doubled_letters.add(a)
                previous_was_double = True
        else:
            previous_was_double = False
    return count >= n


if __name__ == '__main__':
    main()
