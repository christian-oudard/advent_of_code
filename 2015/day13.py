import re
from itertools import permutations


def main():
    graph = read_input('day13_input')

    people = set()
    for a, b in graph.keys():
        people.add(a)
        people.add(b)

    def best_score():
        return max(
            arrangement_score(arrangement, graph)
            for arrangement in permutations(people)
        )

    # Part 1.
    print(best_score())

    # Part 2.
    me = 'Me'
    for p in people:
        graph[(me, p)] = 0
        graph[(p, me)] = 0
    people.add(me)
    print(best_score())


def arrangement_score(people, graph):
    total = 0
    n = len(people)
    for i in range(n):
        j = (i + 1) % n
        a = people[i]
        b = people[j]
        total += graph[(a, b)] + graph[(b, a)]
    return total


def read_input(filename):
    with open(filename) as f:
        lines = f.readlines()

    pattern = re.compile(r'(.+) would (gain|lose) (\d+) happiness units by sitting next to (.+)\.')
    graph = {}
    for line in lines:
        m = pattern.match(line)
        assert m is not None
        a, action, amount, b = m.groups()
        diff = int(amount)
        if action == 'lose':
            diff = -diff
        graph[(a, b)] = diff
    return graph


if __name__ == '__main__':
    main()
