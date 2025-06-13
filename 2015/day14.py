import re
from collections import namedtuple
from dataclasses import dataclass
from typing import Optional


RACE_TIME = 2503


def main():
    specs = list(read_input('day14_input'))
    racers = run_race(specs)

    # Part 1.
    print('Distance')
    racers.sort(key=lambda r: r.distance, reverse=True)
    for place, r in enumerate(racers, 1):
        print(f'{place} - {r.name}: {r.distance}')
    print()

    # Part 2.
    print('Points')
    racers.sort(key=lambda r: r.points, reverse=True)
    for place, r in enumerate(racers, 1):
        print(f'{place} - {r.name}: {r.points}')
    print()


def run_race(specs):
    racers = [ Racer(spec) for spec in specs ]
    for r in racers:
        r.fly()
    for t in range(1, RACE_TIME + 1):
        for r in racers:
            r.step()
        best = max(racers, key=lambda r: r.distance)
        all_best = [ r for r in racers if r.distance == best.distance ]
        for r in all_best:
            r.points += 1
    return racers


ReindeerSpec = namedtuple('Reindeer', 'name speed duration rest')


@dataclass
class Racer:
    spec: ReindeerSpec
    distance: int = 0
    points: int = 0
    fly_duration: Optional[int] = None
    rest_duration: Optional[int] = None

    @property
    def name(self):
        return self.spec.name

    def fly(self):
        self.fly_duration = self.spec.duration
        self.rest_duration = None

    def rest(self):
        self.fly_duration = None
        self.rest_duration = self.spec.rest

    def step(self):
        if self.fly_duration is not None:
            self.fly_duration -= 1
            self.distance += self.spec.speed
            if self.fly_duration == 0:
                self.rest()
        elif self.rest_duration is not None:
            self.rest_duration -= 1
            if self.rest_duration == 0:
                self.fly()


def read_input(filename):
    pattern = re.compile(r'(.+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds.')
    with open(filename) as f:
        for line in f.readlines():
            m = pattern.match(line)
            assert m is not None
            name, speed, duration, rest = m.groups()
            yield ReindeerSpec(name, int(speed), int(duration), int(rest))


if __name__ == '__main__':
    main()
