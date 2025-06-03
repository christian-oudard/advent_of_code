"""
>>> bindings = '''\\
... 123 -> x
... 456 -> y
... x AND y -> d
... x OR y -> e
... x LSHIFT 2 -> f
... y RSHIFT 2 -> g
... NOT x -> h
... NOT y -> i'''.splitlines()
>>> e = Evaluator(bindings)
>>> for name in sorted(e.bindings.keys()):
...     print(f'{name}: {e.evaluate(name)}')
d: 72
e: 507
f: 492
g: 114
h: 65412
i: 65079
x: 123
y: 456
"""


class Evaluator:

    def __init__(self, bindings):
        self.bindings = {}
        self.values = {}
        for line in bindings:
            self.add_binding(line)

    def add_binding(self, line):
        line = line.strip()
        expr, name = line.split(' -> ')
        assert name not in self.bindings
        self.bindings[name] = expr

    def evaluate(self, expr, name=None):
        if name is not None:
            try:
                return self.values[name]
            except KeyError:
                pass

        val = self._evaluate(expr)

        # Convert value to a 16 bit unsigned integer.
        val = val % (1 << 16)

        if name is not None:
            self.values[name] = val
        return val

    def _evaluate(self, expr):
        terms = expr.split()
        if len(terms) == 1:
            # Either an integer or a single variable.
            v = terms[0]
            if v in self.bindings:
                return self.evaluate(self.bindings[v], name=v)
            else:
                return int(v)
        elif len(terms) == 2:
            op, b = terms
            assert op == 'NOT', op
            b = self.evaluate(b)
            return ~b
        elif len(terms) == 3:
            a, op, b = terms
            a = self.evaluate(a)
            b = self.evaluate(b)
            if op == 'AND':
                return a & b
            elif op == 'OR':
                return a | b
            elif op == 'LSHIFT':
                return a << b
            elif op == 'RSHIFT':
                return a >> b
            else:
                raise ValueError(f'Unrecognized operator: {op}')
        else:
            raise ValueError(f'Unrecognized expression: {expr}')


if __name__ == '__main__':
    with open('day07_input') as f:
        e = Evaluator(f.readlines())

    # Part 1.
    a1 = e.evaluate('a')
    print(a1)

    # Part 2.
    e.values = {}
    e.bindings['b'] = str(a1)
    a2 = e.evaluate('a')
    print(a2)

