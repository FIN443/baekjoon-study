import sys


T = int(sys.stdin.readline())
pos = []
for i in range(T):
    a, b = map(int, sys.stdin.readline().split())
    pos.append((a, b))

pos = sorted(pos, key=lambda x: (x[1], x[0]))

[print(i[0], i[1]) for i in pos]
