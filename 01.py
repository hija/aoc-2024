import numpy as np

lines = open('data/01.txt').readlines()

v1 = np.array([])
v2 = np.array([])

for line in lines:
    elms = line.split()
    v1 = np.append(v1, int(elms[0]))
    v2 = np.append(v2, int(elms[1]))

v1.sort()
v2.sort()
print('P1', np.sum(np.abs(v1-v2)))

t1, t2 = np.unique_counts(v2)
v2_counts = dict(zip(t1.tolist(), t2.tolist()))

s = 0
for v in v1:
    s += v * v2_counts.get(v, 0)
print('P2', s)