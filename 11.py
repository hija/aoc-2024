import math


class Conway:

    def __init__(self, elements):
        self.elements = elements
    
    def _split_number_in_two_parts(number_of_digits: int, num: int) -> tuple[int, int]:
        firstpart = num // (10 ** (number_of_digits//2))
        secondpart = num - (firstpart * (10 ** (number_of_digits//2)))
        return (firstpart, secondpart)

    def blink(self):
        new_elements = []
        for element in self.elements:
            if element == 0:
                new_elements.append(1)
                continue
            number_of_digits =  int(math.log10(element))+1
            if number_of_digits % 2 == 0:
                # even
                numbers = Conway._split_number_in_two_parts(number_of_digits, element)
                new_elements.append(numbers[0])
                new_elements.append(numbers[1])
                continue
            new_elements.append(element * 2024)
        self.elements = new_elements

line = [int(x) for x in open("data/11.txt").readline().strip().split()]
cw = Conway(line)
for i in range(25):
    cw.blink()
print('P1', len(cw.elements))