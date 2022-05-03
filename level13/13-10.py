from collections import Counter


T = int(input())
results = []
for _ in range(T):
    T2 = int(input())
    counter = Counter()
    for _ in range(T2):
        _, kind = input().split()
        counter[kind] += 1
    result = 1
    for key in counter.keys():
        result = result * (counter[key] + 1)
    results.append(result - 1)
print(*results, sep="\n")
