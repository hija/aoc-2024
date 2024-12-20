
from dataclasses import dataclass
import itertools

@dataclass
class Position:
    x: int
    y: int
    
    def __hash__(self):
        return hash((self.x,self.y))

AntennaSymbol = str

class AntennaNetwork:

    def __init__(self, lines: list[str]):
        self.antennas: dict[AntennaSymbol, Position] = {}
        self._parse(lines)

    def _parse(self, lines: list[str]):
        for y, line in enumerate(lines):
            for x, c in enumerate(line.strip()):
                if c != '.':
                    existing_antennas = self.antennas.get(c, [])
                    existing_antennas.append(Position(x, y))
                    self.antennas[c] = existing_antennas
        self.max_x = x
        self.max_y = y

    def _is_valid_position(self, x, y):
        return x <= self.max_x and y <= self.max_y and x >= 0 and y >= 0

    def _get_antinodes(self, max_k = 1):
        antinodes = []

        for symbol, positions in self.antennas.items():
            # Combine each position with each other
            for combination in itertools.combinations(positions, 2):
                antenna_1 = combination[0]
                antenna_2 = combination[1]

                diff_x = antenna_2.x - antenna_1.x
                diff_y = antenna_2.y - antenna_1.y

                antinode1 = Position(antenna_1.x - diff_x, antenna_1.y - diff_y)
                antinode2 = Position(antenna_2.x + diff_x, antenna_2.y + diff_y)

                antinodes = antinodes + [antinode1, antinode2]
        
        antinodes = filter(lambda antinode: self._is_valid_position(antinode.x, antinode.y), antinodes)
        return set(antinodes)

    def get_number_of_antinodes(self):
        return len(self._get_antinodes())


    def print_map(self):
        def flatten(xss):
            return [x for xs in xss for x in xs]
        antinodes = self._get_antinodes()
        antenna_positions = flatten([x for (_, x) in self.antennas.items()])

        for y in range(self.max_y + 1):
            for x in range(self.max_x + 1):
                pos = Position(x = x, y = y)
                if pos in antinodes:
                    print('#', end='')
                elif pos in antenna_positions:
                    print('X', end='')
                else:
                    print('.', end='')
            print()


lines = open("data/08.txt").readlines()
an = AntennaNetwork(lines)
print('P1', an.get_number_of_antinodes())