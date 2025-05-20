# A nice string is one with all of the following properties:

# It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
# It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
# It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements.

from itertools import pairwise

VOWELS = 'aeiou'
DISALLOWED = ['ab', 'cd', 'pq', 'xy']

def is_nice_1(s):
    """
    >>> is_nice_1('ugknbfddgicrmopn')
    True
    >>> is_nice_1('aaa')
    True
    >>> is_nice_1('jchzalrnumimnmhp')
    False
    >>> is_nice_1('haegwjzuvuyypxyu')
    False
    >>> is_nice_1('haegwjzuvuyypxyu')
    False
    """
    # At least three vowels.
    vowel_count = sum( 1 for c in s if c in VOWELS)
    if vowel_count < 3:
        return False
    # No disallowed strings.
    if any( d in s for d in DISALLOWED ):
        return False
    # At least one doubled letter.
    for a, b in pairwise(s):
        if a == b:
            return True
    else:
        return False


def is_nice_2(s):
    """
    >>> is_nice_2('qjhvhtzxzqqjkmpb')
    True
    >>> is_nice_2('xxyxx')
    True
    >>> is_nice_2('uurcxstgmygtbstg')
    False
    >>> is_nice_2('ieodomkazucvgmuy')
    False
    """
    # Repeated pair.
    pairs = set()
    for i in range(len(s) - 1):
        pairs.add(s[i:i+2])
    for pair in pairs:
        if s.count(pair) > 1:
            break
    else:
        return False

    # Repeated letter with one space in between.
    for i in range(len(s) - 2):
        a = s[i]
        b = s[i+2]
        if a == b:
            return True
    else:
        return False



if __name__ == '__main__':
    with open('day05_input') as f:
        strings = [ s.strip() for s in f.readlines() ]

    total = 0
    for s in strings:
        if is_nice_1(s):
            total += 1
    print(total)

    total = 0
    for s in strings:
        if is_nice_2(s):
            total += 1
    print(total)
