from itertools import permutations

class RuleAnalyzer:
    def __init__(self):
        self.ruleset = []

    def add_rule(self, rule: str):
        numbers = rule.split('|')
        self.ruleset.append((int(numbers[0]), int(numbers[1])))

    def validate_numers(self, numbers:list[int]):
        for n1 in range(len(numbers)):
            for n2 in range(n1, len(numbers)):
                a = numbers[n1]
                b = numbers[n2]
                if (b, a) in self.ruleset:
                    return (b, a)
        return True
    
    def fix_numbers(self, numbers: list[int]):
        print(numbers)
        rules_affecting_numbers = [x for x in self.ruleset if x[0] in numbers and x[1] in numbers]
        final_order = []
        for number in numbers:
            must_come_before = []
            for rule in rules_affecting_numbers:
                if rule[1] == number and rule[0] in final_order:
                    must_come_before.append(rule[0])
            # get minimum of must_come_before
            indices = [final_order.index(x) for x in must_come_before]
            smallest_must_come_before_index = min(indices) if len(indices) > 0 else 0
            if smallest_must_come_before_index == 0:
                final_order = [number] + final_order
            else:
                print("MCB:", must_come_before)
                print(final_order)
                final_order = final_order[0:smallest_must_come_before_index] + [number] + final_order[smallest_must_come_before_index:]
                print(final_order)
        print()
        print(final_order)
        print(self.validate_numers(final_order))



rule_analyzer = RuleAnalyzer()
is_rule = True

valid_rules_middle = []
fixed_rules_middle = []
for line in open('data/05.txt').readlines():
    if line.strip() == '':
        is_rule = False
        continue
    
    if is_rule:
        rule_analyzer.add_rule(line.strip())
    else:
        numbers = [int(x) for x in line.split(',')]
        if rule_analyzer.validate_numers(numbers) is True:
            valid_rules_middle = valid_rules_middle + [numbers[len(numbers) // 2]]
        else:
            fixed_numbers = rule_analyzer.fix_numbers(numbers)
            fixed_rules_middle = fixed_rules_middle + [fixed_numbers[len(fixed_numbers) // 2]]
            

print('P1', sum(valid_rules_middle))
print('P2', sum(fixed_rules_middle))