import sys

T = int(input())
lst = []
for _ in range(T):
    lst.append(int(sys.stdin.readline()))
print(*sorted(lst), sep="\n")
