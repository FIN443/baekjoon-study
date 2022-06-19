N, M = map(int, input().split())
lst1 = {input(): 1 for _ in range(N)}
lst2 = [input() for _ in range(M)]

result = 0
for s in lst2:
    if s in lst1:
        result += 1
print(result)
