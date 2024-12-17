class Solver:

    def get_combinations(n: int, existing_elements: list[str] = []):
        if n <= 0:
            return existing_elements
        
        elements_to_add = []
        if len(existing_elements) == 0:
            elements_to_add.append("*")
            elements_to_add.append("+")
        else:
            for e in existing_elements:
                elements_to_add.append(e + "*")
                elements_to_add.append(e + "+")
        return Solver.get_combinations(n-1, elements_to_add)

    def _evaluate(components: list[int], operators: str) -> int:
        value = 0
        operator = "+"

        for i in range(len(components)):
            if operator == "+":
                value += components[i]
            elif operator == '*':
                value *= components[i]
            
            if i < len(operators):
                operator = operators[i]
        
        return value

    def get_number_if_can_be_solved(line: str) -> int:
        final_num = int(line.split(": ")[0])
        components = [int(elm) for elm in line.split(": ")[1].split()]

        num_combs = len(components) - 1
        all_combinations = Solver.get_combinations(num_combs)

        for combination in all_combinations:
            if Solver._evaluate(components, combination) == final_num:
                return final_num
        return None


lines = open('data/07.txt').readlines()
print('P1', sum(filter(None, [Solver.get_number_if_can_be_solved(x) for x in lines])))
