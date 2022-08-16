n, m = map(int, input().split())

result = 0
last = []
for _ in range(n):
    P, L = map(int, input().split())
    lst = list(map(int, input().split()))
    lst.sort()
    if L > P:
        last.append(1)
    else:
        last.append(lst[abs(L - P)])

last.sort(reverse=True)
while last:
    v = last.pop()
    if m - v >= 0:
        result += 1
        m -= v
    else:
        break
print(result)
