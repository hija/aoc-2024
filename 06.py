from enum import Enum

class Direction(Enum):
    UP = (0, -1)
    RIGHT = (1, 0)
    DOWN = (0, 1)
    LEFT = (-1, 0)

    def __init__(self, add_x, add_y):
        self.add_x = add_x
        self.add_y = add_y

    def next(self):
        members = list(Direction)
        current_index = members.index(self)
        next_index = (current_index + 1) % len(members)
        return members[next_index]
    
    def to_tuple(self):
        return (self.add_x, self.add_y)

class Postition:

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __add__(self, other: Direction):
        return Postition(self.x + other.add_x, self.y + other.add_y)
    
    def __sub__(self, other: Direction):
        return Postition(self.x - other.add_x, self.y - other.add_y)
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __hash__(self) -> int:
        return hash((self.x, self.y))

    def __repr__(self) -> str:
        return f'x = {self.x}, y = {self.y}'

class Screen:
    def __init__(self) -> None:
        self.lines = []
        self.position = None
        self._direction = Direction.UP
        self.unique_positions = []

    def add_row(self, row):
        self.lines.append(row)

    def _find_starting_point(self) -> tuple[int, int] | None:
        for y, line in enumerate(self.lines):
            for x, column in enumerate(line):
                if column == '^':
                    return (x, y)
    
    def _get_character_at_position(self, pos: Postition):
        for _y, line in enumerate(self.lines):
            for _x, c in enumerate(line):
                if _x == pos.x and _y == pos.y:
                    return c
        return None

    def play(self):
        # True if game continues, False otherwise
        if self.position is None:
            start_x, start_y = self._find_starting_point()
            self.position = Postition(start_x, start_y)
        
        self.unique_positions.append(self.position)
        next_position = self.position + self._direction
        char_at_position = self._get_character_at_position(next_position)

        if char_at_position == '#':
            self._direction = self._direction.next()
        elif not(char_at_position):
            return False
        else:
            self.position = next_position
        
        return True
 
screen = Screen()
[screen.add_row(line) for line in open("data/06.txt").readlines()]

while(screen.play()):
    continue
print('P1: ', len(set(screen.unique_positions)))