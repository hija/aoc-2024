import re

line = ''.join(open("data/03.txt").readlines())
rp = r'(do\(\))|(don\'t\(\))|mul\((\d+),(\d+)\)'

enabled = True
p1 = 0
p2 = 0

for m in re.findall(rp, line):
    if m[0]:
        enabled = True
    elif m[1]:
        enabled = False
    else:
        p1 += int(m[2]) * int(m[3])
        if enabled:
            p2 += int(m[2]) * int(m[3])
print('P1', p1)
print('P2', p2)