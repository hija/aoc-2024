import math


class Conway:

    def __init__(self, elements):
        self.num_digits = {}
        for element in elements:
            element_count = self.num_digits.get(element, 0)
            element_count = element_count + 1
            self.num_digits[element] = element_count
    
    def _split_number_in_two_parts(number_of_digits: int, num: int) -> tuple[int, int]:
        firstpart = num // (10 ** (number_of_digits//2))
        secondpart = num - (firstpart * (10 ** (number_of_digits//2)))
        return (firstpart, secondpart)

    def blink(self):
        new_num_digits = {}
        for element, num in self.num_digits.items():
            if element == 0:
                c = new_num_digits.get(1, 0)
                c = c + num
                new_num_digits[1] = c
                continue
            number_of_digits =  int(math.log10(element))+1
            if number_of_digits % 2 == 0:
                # even
                numbers = Conway._split_number_in_two_parts(number_of_digits, element)
                c1 = new_num_digits.get(numbers[0], 0)
                c1 = c1 + num
                new_num_digits[numbers[0]] = c1

                c2 = new_num_digits.get(numbers[1], 0)
                c2 = c2 + num
                new_num_digits[numbers[1]] = c2
                continue
            
            c = new_num_digits.get(element * 2024, 0)
            c = c + num
            new_num_digits[element * 2024] = c
        self.num_digits = new_num_digits

line = [int(x) for x in open("data/11.txt").readline().strip().split()]
cw = Conway(line)
for i in range(25):
    cw.blink()
print('P1', sum(cw.num_digits.values()))
for i in range(50):
    cw.blink()
print('P2', sum(cw.num_digits.values()))