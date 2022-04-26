import sys


T = int(sys.stdin.readline())
lst = []
for i in range(T):
    a, b = sys.stdin.readline().split()
    lst.append((int(a), b))

lst = sorted(lst, key=lambda x: x[0])

[print(i[0], i[1]) for i in lst]
