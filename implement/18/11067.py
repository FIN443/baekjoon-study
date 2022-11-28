from collections import defaultdict


T = int(input())
for _ in range(T):
    n = int(input())
    results = [[0, 0]]
    caffes_dict = defaultdict(list)
    for _ in range(n):
        x, y = map(int, input().split())
        caffes_dict[x].append(y)

    sorted_caffes = sorted(caffes_dict.items())

    for i in range(len(sorted_caffes)):
        sorted_caffes[i][1].sort()
        if results[-1][1] != sorted_caffes[i][1][0]:
            sorted_caffes[i][1].sort(reverse=True)
        for j in range(len(sorted_caffes[i][1])):
            results.append([sorted_caffes[i][0], sorted_caffes[i][1][j]])

    m = list(map(int, input().split()))

    for j in range(1, len(m)):
        print(*results[m[j]])
