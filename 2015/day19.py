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


def previous_molecule(molecule, replacements):
    """
    Find a replacement that would generate the current molecule. Prioritize larger replacements.

    >>> replacements = [('H', ['H', 'O']), ('H', ['O', 'H']), ('O', ['H', 'H']), ('e', ['H']), ('e', ['O'])]
    >>> previous_molecule(split_molecule('HO'), replacements)
    ['H']
    """
    molecule = list(molecule)
    for before, after in replacements:
        idx = find_subsequence(after, molecule)
        if idx is None:
            continue
        molecule[idx : idx + len(after)] = [before]
        print(f'{join_molecule(after)} => {before}')
        return molecule

    raise ValueError(f"No previous molecule for {join_molecule(molecule)}")


def num_distinct(molecules):
    return len(set(tuple(mol) for mol in molecules))


def search_molecule(molecule, replacements):
    """
    >>> replacements = [('H', ['H', 'O']), ('H', ['O', 'H']), ('O', ['H', 'H']), ('e', ['H']), ('e', ['O'])]
    >>> search_molecule(split_molecule('HOHOHO'), replacements)
    6
    """
    # Identify atoms which only appear on the right side of replacements. Sort the replacements to prioritize these.
    left_side_atoms = set( l for l, _ in replacements )
    right_side_atoms = set( r for _, rs in replacements for r in rs )
    right_side_only = right_side_atoms - left_side_atoms
    replacements.sort(key=lambda x: -any( r in right_side_only for r in x[1] ))

    # Work backward from the end.
    count = 0
    print(join_molecule(molecule))
    while molecule != ['e']:
        molecule = previous_molecule(molecule, replacements)
        print(join_molecule(molecule))
        count += 1
    return count


# def search_molecule(final, replacements):
#     """
#     """
#     final = final
#     len_final = len(final)
#     molecules = {('e',)}
#     for i in count():
#         print(i, len(molecules))
#         for m in molecules:
#             print(join_molecule(m))
#         if any( m == final for m in molecules ):
#             break
#         molecules = {
#             m for m in molecules
#             if len(m) < len_final
#         }
#         next_set = set()
#         for m in molecules:
#             next_set.update(next_molecules(m, replacements))
#         molecules = next_set
#     return i


if __name__ == '__main__':
    target, replacements = read_input()

    # Part 1.
    print(num_distinct(next_molecules(target, replacements)))

    # Part 2.
    print(search_molecule(target, replacements))
