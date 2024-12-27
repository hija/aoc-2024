
from collections import namedtuple

MatrixPosition = namedtuple("MatrixPosition", ("x", "y"))
VisitedPosition = namedtuple("VisitedPosition", ("value_to_find", "x", "y"))

class HeightMap:
    
    def __init__(self, width: int, height: int):
        self._init_height_map(width=width, height=height)

    def _init_height_map(self, width: int, height: int):
        self.map = []
        for _ in range(height):
            row = []
            for _ in range(width):
                row.append(0)
            self.map.append(row)

    def print(self):
        for row in self.map:
            print(*row, sep='\t')


class Maze:
    
    def __init__(self, lines: list[str]):
        self.trailmaxs = []
        self.trailheads = []
        self._height_map_part1 = HeightMap(len(lines[0].strip()), len(lines))
        self._height_map_part2 = HeightMap(len(lines[0].strip()), len(lines))
        self._parse(lines)
        for trailmax in self.trailmaxs:
            self._update_heightmap_part_1(trailmax.x, trailmax.y, value_to_find=9, visited=[])
            self._update_heightmap_part_2(trailmax.x, trailmax.y, value_to_find=9)
    
    @property
    def score_part1(self):
        score = 0
        for trailhead in self.trailheads:
            score += self._height_map_part1.map[trailhead.y][trailhead.x]
        return score

    @property
    def score_part2(self):
        score = 0
        for trailhead in self.trailheads:
            score += self._height_map_part2.map[trailhead.y][trailhead.x]
        return score

    @property
    def width(self):
        return len(self.map) - 1
    
    @property
    def height(self):
        return len(self.map[0]) - 1

    def _update_heightmap_part_1(self, x: int, y:int, value_to_find: int = 9, visited: list[MatrixPosition] = []):
        position = VisitedPosition(value_to_find=value_to_find, x = x, y = y)
        if position in visited:
            return
        
        visited.append(position)

        if value_to_find < 0:
            return
        
        if x < 0 or y < 0:
            return
        
        if x > self.width or y > self.height:
            return

        if value_to_find == self.map[y][x]:
            # Update in all directions
            self._height_map_part1.map[y][x] = self._height_map_part1.map[y][x] + 1
            self._update_heightmap_part_1(x-1, y, value_to_find-1, visited)
            self._update_heightmap_part_1(x+1, y, value_to_find-1, visited)
            self._update_heightmap_part_1(x, y-1, value_to_find-1, visited)
            self._update_heightmap_part_1(x, y+1, value_to_find-1, visited)
    
    def _update_heightmap_part_2(self, x: int, y:int, value_to_find: int = 9):
        if value_to_find < 0:
            return
        
        if x < 0 or y < 0:
            return
        
        if x > self.width or y > self.height:
            return

        if value_to_find == self.map[y][x]:
            # Update in all directions
            self._height_map_part2.map[y][x] = self._height_map_part2.map[y][x] + 1
            self._update_heightmap_part_2(x-1, y, value_to_find-1)
            self._update_heightmap_part_2(x+1, y, value_to_find-1)
            self._update_heightmap_part_2(x, y-1, value_to_find-1)
            self._update_heightmap_part_2(x, y+1, value_to_find-1)


    def _parse(self, lines: list[str]):
        self.map = []
        for y, line in enumerate(lines):
            elements = []
            for x, el in enumerate(line.strip()):
                if el.isalnum():
                    el_as_numeric = int(el)
                    elements.append(el_as_numeric)
                    if el_as_numeric == 9:
                        self.trailmaxs.append(MatrixPosition(x = x, y = y))
                    elif el_as_numeric == 0:
                        self.trailheads.append(MatrixPosition(x = x, y = y))
                else:
                    elements.append(int(-1))
            self.map.append(elements)

    def print(self):
        for row in self.map:
            print(*row, sep='\t')



maze = Maze(open("data/10.txt").readlines())
print('P1', maze.score_part1)
print('P2', maze.score_part2)