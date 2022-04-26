import sys


T = int(sys.stdin.readline())
D = {}
for i in range(T):
    s = sys.stdin.readline().strip()
    D[s] = len(s)

D = sorted(sorted(D.items()), key=lambda x: x[1])

[print(i[0]) for i in D]
