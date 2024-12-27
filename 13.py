import z3

def solve(abutton_x, abutton_y, bbutton_x, bbutton_y, target_x, target_y):
    abutton_presses = z3.Int('a')
    bbutton_presses = z3.Int('b')
    
    optimizer = z3.Optimize()
    optimizer.add(abutton_presses * abutton_x + bbutton_presses * bbutton_x == target_x)
    optimizer.add(abutton_presses * abutton_y + bbutton_presses * bbutton_y == target_y)
    optimizer.minimize(abutton_presses + bbutton_presses)
    
    if optimizer.check().r == z3.Z3_L_TRUE:
        m = optimizer.model()
        return m[abutton_presses].as_long() * 3 + m[bbutton_presses].as_long()
    return 0


### Part 1
s = 0
for line in open("data/13.txt").readlines():
    if line.startswith('Button A: '):
        abutton_x = int(line.split('X+')[1].split(',')[0])
        abutton_y = int(line.split('Y+')[1].strip())
    elif line.startswith('Button B: '):
        bbutton_x = int(line.split('X+')[1].split(',')[0])
        bbutton_y = int(line.split('Y+')[1].strip())
    elif line.startswith('Prize: '):
        target_x = int(line.split('X=')[1].split(',')[0])
        target_y = int(line.split('Y=')[1].strip())
        s += solve(abutton_x=abutton_x, abutton_y=abutton_y, bbutton_x=bbutton_x, bbutton_y=bbutton_y, target_x=target_x, target_y=target_y)

print('P1', s)

### Part 2
s = 0
for line in open("data/13.txt").readlines():
    if line.startswith('Button A: '):
        abutton_x = int(line.split('X+')[1].split(',')[0])
        abutton_y = int(line.split('Y+')[1].strip())
    elif line.startswith('Button B: '):
        bbutton_x = int(line.split('X+')[1].split(',')[0])
        bbutton_y = int(line.split('Y+')[1].strip())
    elif line.startswith('Prize: '):
        target_x = int(line.split('X=')[1].split(',')[0]) + 10000000000000
        target_y = int(line.split('Y=')[1].strip()) + 10000000000000
        s += solve(abutton_x=abutton_x, abutton_y=abutton_y, bbutton_x=bbutton_x, bbutton_y=bbutton_y, target_x=target_x, target_y=target_y)

print('P2', s)