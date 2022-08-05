N, L = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()

prev = lst[0]
start = lst[0]
count = 0
for pos in lst:
    if pos - start > L - 1:
        count += 1
        start = pos
    prev = pos

if pos - start <= L - 1:
    count += 1

print(count)

""" while문
count = 0
idx = 0
while idx < len(lst):
    count += 1
    prev = lst[idx]
    while True:
        idx += 1
        if idx >= len(lst) or lst[idx] >= prev + L:
            break 
"""
