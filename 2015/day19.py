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
    ('Si', 'Rn', 'F', 'Ar')
    """
    return tuple(
        atom for atom in
        re.split(r'([A-Z][a-z]?)', s)
        if atom != ''
    )


def join_molecule(atoms):
    return ''.join(atoms)


def next_molecules(start, replacements):
    """
    >>> replacements = {'H': [('H', 'O'), ('O', 'H')], 'O': [('H', 'H')]}
    >>> [ join_molecule(m) for m in sorted(set(next_molecules(split_molecule('HOH'), replacements))) ]
    ['HHHH', 'HOHO', 'HOOH', 'OHOH']
    >>> len(set(next_molecules(split_molecule('HOHOHO'), replacements)))
    7
    """
    for i, c in enumerate(start):
        for repl in replacements.get(c, []):
            next_molecule = list(start)
            next_molecule[i:i+1] = list(repl)
            yield tuple(next_molecule)


def search_molecule(final, replacements):
    """
    >>> replacements = {'e': [('H',), ('O',)], 'H': [('H', 'O'), ('O', 'H')], 'O': [('H', 'H')]}
    >>> search_molecule(split_molecule('HOHOHO'), replacements)
    6
    """
    final = final
    len_final = len(final)
    molecules = {('e',)}
    for i in count():
        print(i, len(molecules))
        for m in molecules:
            print(join_molecule(m))
        if any( m == final for m in molecules ):
            break
        molecules = {
            m for m in molecules
            if len(m) < len_final
        }
        next_set = set()
        for m in molecules:
            next_set.update(next_molecules(m, replacements))
        molecules = next_set
    return i


if __name__ == '__main__':
    target, replacements = read_input()

    # Part 1.
    print(len(set(next_molecules(target, replacements))))

    # Part 2.
    print(search_molecule(target, replacements))
