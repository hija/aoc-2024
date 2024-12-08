checked_pos = []

class Matrix:

    def __init__(self):
        self.data = []
        
    def add_row(self, row):
        self.data.append(row)

    def get_character(self, x, y):
        if y < 0 or y >= len(self.data):
            return '' # return empty
        row = self.data[y]

        if x < 0 or x >= len(row):
            return ''
        
        return row[x]
    
    def print_masked(self, mask):
        for y in range(len(self.data)):
            for x in range(len(self.data[0])):
                if (x,y) in mask:
                    print(self.get_character(x, y), end='')
                else:
                    print('.', end='')
            print()

def check_solution(matrix, x, y, remaining_letters, x_add, y_add, pos = [], debug=False):
    global checked_pos

    if debug:
        print(f'{x=} {y=} {remaining_letters=} get_character={matrix.get_character(x, y)}')
    if len(remaining_letters) == 0:
        checked_pos = checked_pos + pos
        return 1
    relevant_character = remaining_letters[0]
    if matrix.get_character(x, y) == relevant_character:
        return check_solution(matrix, x + x_add, y + y_add, remaining_letters[1:], x_add, y_add, pos +[(x, y)])
    else:
        return 0

matrix = Matrix()
lines = open('data/04.txt').readlines()
for line in lines:
    matrix.add_row(line)

height = len(lines)
width = len(lines[0])
result = 0
for y in range(height):
    for x in range(width):
        result += check_solution(matrix, x, y, 'XMAS', 1, 0) # nach vorne
        result += check_solution(matrix, x, y, 'XMAS', -1, 0) # nach hinten
        result += check_solution(matrix, x, y, 'XMAS', 0, 1) # nach unten
        result += check_solution(matrix, x, y, 'XMAS', 0, -1) # nach oben

        result += check_solution(matrix, x, y, 'XMAS', 1, 1) # nach vorne unten
        result += check_solution(matrix, x, y, 'XMAS', 1, -1) # nach vorne oben
        result += check_solution(matrix, x, y, 'XMAS', -1, 1) # nach hinten unten
        result += check_solution(matrix, x, y, 'XMAS', -1, -1) # nach hinten oben
print('P1', result)
# matrix.print_masked(checked_pos)

result = 0
for y in range(height):
    for x in range(width):
        if matrix.get_character(x, y) == 'A':
            d1 = [matrix.get_character(x-1, y-1), matrix.get_character(x+1, y+1), 'A']
            d2 = [matrix.get_character(x-1, y+1), matrix.get_character(x+1, y-1), 'A']
            if sorted(d1) == ['A', 'M', 'S'] and sorted(d2) == ['A', 'M', 'S']:
                result += 1
        
print('P2', result)