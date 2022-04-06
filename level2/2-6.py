import math


h, m = input().split()
h = int(h)
m = int(m)
i = int(input())
i_m = math.floor((m + i) / 60)

if m + i >= 60:
    m = (m + i) % 60
    if h + i_m > 23:
        h = (h + i_m) % 24
    else:
        h = h + i_m
else:
    m = m + i
print(h, m)
