import sys


T = int(sys.stdin.readline())
pos = []
for i in range(T):
    a, b = map(int, sys.stdin.readline().split())
    pos.append((a, b))

pos = sorted(pos, key=lambda x: (x[0], x[1]))

[print(i[0], i[1]) for i in pos]


"""
# (-100,000 ≤ xi, yi ≤ 100,000)
import sys

N = int(input())
coords = []
for i in range(N):
    x,y = map(int,sys.stdin.readline().split())
    coords.append((x,y))

for coord in sorted(coords):
    print(coord[0],coord[1])
"""
