import re


def read_input():
    with open('day19_input') as f:
        lines = f.read().splitlines()

    starting_molecule = lines.pop(-1)
    assert lines.pop(-1) == ''
    starting_molecule = split_molecule(starting_molecule)

    replacements = []
    for line in lines:
        before, after = line.split(' => ')
        replacements.append((before, split_molecule(after)))

    return starting_molecule, replacements


def split_molecule(s):
    """
    >>> split_molecule('Ca')
    ['Ca']
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
    >>> replacements = [('H', ('H', 'O')), ('H', ('O', 'H')), ('O', ('H', 'H'))]
    >>> num_distinct(next_molecules(split_molecule('HOH'), replacements))
    4
    >>> num_distinct(next_molecules(split_molecule('HOHOHO'), replacements))
    7
    """
    for i, atom in enumerate(start):
        for before, after in replacements:
            if atom == before:
                next_molecule = list(start)
                next_molecule[i:i+1] = after
                yield next_molecule


def find_subsequence(needle, haystack):
    """
    Find the first occurrence of `needle` in `haystack`.
    Return the index where it is found, or None if it is not there.

    >>> find_subsequence([7, 2, 9], [2, 9, 7, 2, 9, 3, 5])
    2
    >>> find_subsequence([2, 7, 9], [2, 9, 7, 2, 9, 3, 5]) is None
    True
    >>> find_subsequence(['H', 'O'], ['H', 'O'])
    0
    """
    needle_size = len(needle)
    for offset in range(len(haystack) - needle_size + 1):
        if haystack[offset: offset + needle_size] == needle:
            return offset
    return None


def num_distinct(molecules):
    return len(set(tuple(mol) for mol in molecules))


def search_molecule(molecule, replacements):
    # This is actually a terribly written problem, because it relies on a particular structure of the target molecule.
    # Real search algorithms like DFS and A* fail terribly here.
    steps = 0
    while molecule != ['e']:
        changed = False
        for before, after in replacements:
            idx = find_subsequence(after, molecule)
            if idx is not None:
                molecule = molecule[:idx] + [before] + molecule[idx + len(after):]
                steps += 1
                changed = True
        if not changed:
            raise RuntimeError('No valid replacements left.')
    return steps


if __name__ == '__main__':
    target, replacements = read_input()

    # Part 1.
    print(num_distinct(next_molecules(target, replacements)))

    # Part 2.
    print(search_molecule(target, replacements))

