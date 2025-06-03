"""
>>> nodes, distances = parse_graph('''
... London to Dublin = 464
... London to Belfast = 518
... Dublin to Belfast = 141
... ''')
>>> nodes = sorted(nodes)
>>> nodes
['Belfast', 'Dublin', 'London']
>>> distances
{('Dublin', 'London'): 464, ('Belfast', 'London'): 518, ('Belfast', 'Dublin'): 141}
>>> shortest_and_longest_hamiltonian_path(nodes, distances)
(('Belfast', 'Dublin', 'London'), 605, ('Belfast', 'London', 'Dublin'), 982)
"""


from itertools import permutations, pairwise


def parse_graph(input_string):
    nodes = set()
    distances = {}
    for line in input_string.strip().splitlines():
        line = line.strip()
        locations, distance = line.split(' = ')

        a, b = locations.split(' to ')
        a, b = sorted((a, b))
        nodes.add(a)
        nodes.add(b)

        distance = int(distance)
        distances[(a, b)] = distance

    return nodes, distances


def shortest_and_longest_hamiltonian_path(nodes, distances):
    # Try all permutations of nodes via brute force.
    best_perm = None
    best_dist = None
    worst_perm = None
    worst_dist = None
    for perm in permutations(nodes):
        dist = 0
        for a, b in pairwise(perm):
            a, b = sorted((a, b))
            dist += distances[(a, b)]
        if best_dist is None or dist < best_dist:
            best_perm = perm
            best_dist = dist
        if worst_dist is None or dist > worst_dist:
            worst_perm = perm
            worst_dist = dist
    return best_perm, best_dist, worst_perm, worst_dist


if __name__ == '__main__':
    input_string = open('day09_input').read()
    nodes, distances = parse_graph(input_string)
    best_path, best_dist, worst_path, worst_dist = shortest_and_longest_hamiltonian_path(nodes, distances)
    print(f'{" -> ".join(best_path)} = {best_dist}')
    print(f'{" -> ".join(worst_path)} = {worst_dist}')




