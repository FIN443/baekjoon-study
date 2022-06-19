import sys


T = int(sys.stdin.readline())
D = {}
for i in range(T):
    s = sys.stdin.readline().strip()
    D[s] = len(s)

D = sorted(sorted(D.items()), key=lambda x: x[1])

[print(i[0]) for i in D]


"""
import sys
n = int(input())
num_list = []

for i in range(n):
    str1 = sys.stdin.readline().strip()
    num_list.append(str1)
a = set(num_list)
num_list = list(a)

num_list.sort(key= lambda x : [len(x), x])
for i in num_list:
    print(i)
"""
