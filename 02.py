import numpy as np

lines = open('data/02.txt').readlines()

def is_safe(row):
    is_ascending = np.sum(row) > 0
    if is_ascending:
        return np.max(v) <= 3 and np.min(v) >= 1
    else:
        return np.min(v) >= -3 and np.max(v) <= -1

p1 = 0
p2 = 0
for line in lines:
    v1 = [int(x) for x in line.split()]
    v = np.diff(np.array(v1))
    p1 += is_safe(v)

    # P2 (ugly but works lol)

    # Find positions to fix
    is_ascending = np.sum(v) > 0
    if is_ascending:
        wrong_positions = np.where((v < 1) | (v > 3))
    else:
        wrong_positions = np.where((v < -3) | (v > -1))
    
    # Fix at -1, 0  or 1
    if len(wrong_positions[0]) > 0:
        try:
            
            v2 = np.delete(v1, [wrong_positions[0][0] + 1], axis=0)
            v = np.diff(v2)
            if is_safe(v):
                p2 += 1
                continue
        except:
            pass
        try:
            
            v2 = np.delete(v1, [wrong_positions[0][0] + 0], axis=0)
            v = np.diff(v2)
            if is_safe(v):
                p2 += 1
                continue
        except:
            pass
    
        try:
            v2 = np.delete(v1, [wrong_positions[0][0] - 1], axis=0)
            v = np.diff(v2)
            if is_safe(v):
                p2 += 1
                continue
        except:
            pass

    else:
        p2 += 1 if is_safe(v) else 0
        


print(p1)
print(p2)