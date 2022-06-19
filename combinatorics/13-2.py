# N % A == 0
# A != 1 and A != N


T = int(input())
lst = list(map(int, input().split()))

c = min(lst)
if c < 2:
    print(max(lst) * 2)
else:
    print(max(lst) * c)
