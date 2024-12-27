from collections import namedtuple


Position = namedtuple("Position", ("x", "y"))

class Garden:
    
    def __init__(self, lines: list[str]):
        self._parse(lines)
        
    def _parse(self, lines: list[str]):
        self.map = []
        for line in lines:
            self.map.append([x for x in line.strip()])

    def _get_character_at_position(self, x, y):
        if x < 0 or y < 0:
            return None
        if x > len(self.map) - 1 or y > len(self.map) - 1:
            # len(self.map) is width/height since the garden is a square
            return None
        
        return self.map[y][x]

    @property
    def score(self):
        
        position_in_regionmaps = []

        def walk(c: str, x: int, y: int, visited: list[Position] = [], region_map: list[Position] = []):
            current_position = Position(x=x, y = y)
            character_at_position = self._get_character_at_position(x, y)
            if current_position in visited or character_at_position is None or character_at_position != c:
                return region_map
            
            position_in_regionmaps.append(current_position)
            visited.append(current_position)
            region_map.append(current_position)
            
            region_map.extend(walk(c, x-1, y, visited, []))
            region_map.extend(walk(c, x+1, y, visited, []))
            region_map.extend(walk(c, x, y-1, visited, []))
            region_map.extend(walk(c, x, y+1, visited, []))
            return region_map


        score = 0
        for y in range(len(self.map)):
            for x in range(len(self.map)):
                current_position = Position(x=x, y=y)
                if current_position in position_in_regionmaps:
                    continue
                else:
                    current_character = self._get_character_at_position(current_position.x, current_position.y)
                    region = walk(current_character, current_position.x, current_position.y, [], [])
                    perimeter_of_region = sum([self._get_perimeter_addition(pos.x, pos.y) for pos in region])
                    score += perimeter_of_region * len(region)
        return score
                

    def _get_perimeter_addition(self, x, y):
        t = self._get_character_at_position(x, y-1)

        l = self._get_character_at_position(x-1, y)
        current_character = self._get_character_at_position(x, y)
        r = self._get_character_at_position(x+1, y)
        
        b = self._get_character_at_position(x, y+1)

        # There are 9 different constellations
        differences = sum(map(lambda x: x != current_character, [t, l, r, b]))
        return differences

garden = Garden(open("data/12.txt").readlines())
print('P1', garden.score)