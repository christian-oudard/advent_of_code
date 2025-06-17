ON_CHAR = '#'
OFF_CHAR = '.'
ON = True
OFF = False

class ConwayLife:
    def __init__(self, array):
        self.array = array
        self.height = len(array)
        self.width = len(array[0])
        assert all( len(row) == self.width for row in array)

    @classmethod
    def from_string(cls, input_string):
        array = []
        for line in input_string.strip().splitlines():
            row = []
            for c in line:
                if c == ON_CHAR:
                    row.append(ON)
                elif c == OFF_CHAR:
                    row.append(OFF)
            array.append(row)
        return cls(array)

    def __str__(self):
        output_lines = []
        for row in self.array:
            output_row = []
            for c in row:
                if c == ON:
                    output_row.append(ON_CHAR)
                elif c == OFF:
                    output_row.append(OFF_CHAR)
            output_lines.append(''.join(output_row))
        return '\n'.join(output_lines)

    def get(self, p):
        x, y = p
        if (
            x < 0 or x >= self.width
            or y < 0 or y >= self.height
        ):
            return OFF
        return self.array[y][x]

    def neighbors(self, p):
        x, y = p
        for dx, dy in [
            (-1, -1),
            ( 0, -1),
            (+1, -1),
            (+1,  0),
            (+1, +1),
            ( 0, +1),
            (-1, +1),
            (-1,  0),
        ]:
            yield (x + dx, y + dy)

    def neighbor_count(self, p):
        return sum(
            1
            for n in self.neighbors(p)
            if self.get(n)
        )

    def cells(self):
        for y, row in enumerate(self.array):
            for x, c in enumerate(row):
                yield (x, y), c

    def corners(self):
        return [
            (0, 0),
            (self.width - 1, 0),
            (0, self.height - 1),
            (self.width - 1, self.height - 1),
        ]

    def step(self, corners_stuck=False):
        next_array = [ [ None for x in range(self.width) ] for y in range(self.height) ]

        if corners_stuck:
            for p in self.corners():
                x, y = p
                self.array[y][x] = ON

        for p, c in self.cells():
            neighbor_count = self.neighbor_count(p)
            if c == ON:
                if neighbor_count in [2, 3]:
                    next_cell = ON
                else:
                    next_cell = OFF
            elif c == OFF:
                if neighbor_count == 3:
                    next_cell = ON
                else:
                    next_cell = OFF

            x, y = p
            next_array[y][x] = next_cell

        if corners_stuck:
            for p in self.corners():
                x, y = p
                next_array[y][x] = ON

        self.array = next_array

    def count_lights(self):
        return sum( 1 for _, c in self.cells() if c == ON )


if __name__ == '__main__':
    import time

    with open('day18_input') as f:
        input_string = f.read()

    # Part 1.
    board = ConwayLife.from_string(input_string)
    print(board)
    for _ in range(100):
        board.step()
        time.sleep(0.1)
        print()
        print(board)
    part_1_count = board.count_lights()

    # Part 2.
    board = ConwayLife.from_string(input_string)
    print(board)
    for _ in range(100):
        board.step(corners_stuck=True)
        time.sleep(0.1)
        print()
        print(board)
    part_2_count = board.count_lights()

    print()
    print('Part 1', part_1_count)
    print('Part 2', part_2_count)
