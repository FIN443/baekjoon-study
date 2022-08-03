N = int(input())
lst = []
for _ in range(N):
    lst.append(list(map(int, input().split())))

result = max(lst, key=lambda x: x[0])[0] - min(lst, key=lambda x: x[1])[1]

if result < 0:
    print(0)
else:
    print(result)


"""
import sys
input = sys.stdin.readline

N = int(input())
lst = []

for _ in range(N):
    s,e = map(int,input().split())
    lst.append((s,e))

left = lst[0][0]
right = lst[0][1]

for i in range(1,N):
    if left < lst[i][0]:
        left = lst[i][0]
    if right > lst[i][1]:
        right = lst[i][1]

if left <= right:
    print(0)
else:
    print(left-right)
"""
