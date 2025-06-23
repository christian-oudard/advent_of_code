import re
from itertools import count


def read_input():
    with open('day19_input') as f:
        lines = f.read().splitlines()

    starting_molecule = lines.pop(-1)
    assert lines.pop(-1) == ''

    replacements = {}
    for line in lines:
        before, after = line.split(' => ')
        replacements.setdefault(before, []).append(after)

    return starting_molecule, replacements


def split_molecule(s):
    """
    >>> split_molecule('SiRnFAr')
    ['Si', 'Rn', 'F', 'Ar']
    """
    return [
        atom for atom in
        re.split(r'([A-Z][a-z]?)', s)
        if atom != ''
    ]


def join_molecule(atoms):
    return ''.join(atoms)


def next_molecules(start, replacements):
    """
    >>> replacements = {'H': ['HO', 'OH'], 'O': ['HH']}
    >>> sorted(set(next_molecules('HOH', replacements)))
    ['HHHH', 'HOHO', 'HOOH', 'OHOH']
    >>> len(set(next_molecules('HOHOHO', replacements)))
    7
    """
    start = split_molecule(start)
    replacements = {
        c: [ split_molecule(repl) for repl in repls ]
        for c, repls in replacements.items()
    }
    for i, c in enumerate(start):
        for repl in replacements.get(c, []):
            next_molecule = list(start)
            next_molecule[i:i+1] = list(repl)
            s = join_molecule(next_molecule)
            yield s


def previous_molecules(start, replacements):
    """
    >>> replacements = {'H': ['HO', 'OH'], 'O': ['HH']}
    >>> sorted(set(previous_molecules('HOH', replacements)))
    ['HH']
    """
    start = split_molecule(start)
    replacements = {
        c: [ split_molecule(repl) for repl in repls ]
        for c, repls in replacements.items()
    }
    for c, repls in replacements.items():
        for repl in repls:
            for i in find_all(repl, start):
                prev_molecule = list(start)
                prev_molecule[i:i+len(repl)] = [c]
                if len(prev_molecule) > 1 and 'e' in prev_molecule:
                    continue
                s = join_molecule(prev_molecule)
                yield s


def find_all(needle, haystack):
    """
    >>> list(find_all('abc', 'xxabcxx'))
    [2]
    >>> list(find_all('xxx', 'xxabcxx'))
    []
    >>> list(find_all('xx', 'xxxabxx'))
    [0, 1, 5]
    """
    assert len(needle) > 0
    needle_len = len(needle)
    for i in range(len(haystack) - needle_len + 1):
        if haystack[i:i+needle_len] == needle:
            yield i



def search_molecule(final, replacements):
    """
    >>> replacements = {'e': ['H', 'O'], 'H': ['HO', 'OH'], 'O': ['HH']}
    >>> search_molecule('HOHOHO', replacements)
    6
    """
    molecules = {final}
    for i in count():
        print(i, len(molecules))
        assert len(molecules) > 0
        # for m in molecules:
        #     print(m)
        if any( m == 'e' for m in molecules ):
            break
        prev_molecules = set()
        for m in molecules:
            prev_molecules.update(previous_molecules(m, replacements))
        molecules = prev_molecules
    return i


if __name__ == '__main__':
    target, replacements = read_input()

    # Part 1.
    print(len(set(next_molecules(target, replacements))))

    # Part 2.
    print(search_molecule(target, replacements))
