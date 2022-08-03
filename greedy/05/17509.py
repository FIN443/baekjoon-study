lst = []
for _ in range(11):
    D, V = map(int, input().split())
    lst.append((D, V))

lst.sort(key=lambda x: x[0])
accum = 0
penalty = 0
for i, j in lst:
    penalty += i + accum
    if j > 0:
        penalty += j * 20
    accum += i

print(penalty)
