T = int(input())
results = []

for _ in range(T):
    n = int(input())
    lst = [1, 1, 1]
    for i in range(4, n + 1):
        result1 = lst[0] + lst[1]
        lst[0] = lst[1]
        lst[1] = lst[2]
        lst[2] = result1
    results.append(lst[2])

print(*results, sep="\n")
