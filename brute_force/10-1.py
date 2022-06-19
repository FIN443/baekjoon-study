# M을 넘지 않으면서 M에 최대한 가까운 카드 3장의 합
# 첫째 줄에 카드의 개수 N(3 ≤ N ≤ 100)과 M(10 ≤ M ≤ 300,000)

N, M = map(int, input().split())
lst = []
lst = list(map(int, input().split()))
lst = sorted(lst, reverse=True)
line = len(lst)
result = 0
for i in range(line):
    for j in range(i + 1, line, 1):
        for k in range(j + 1, line, 1):
            if result <= lst[i] + lst[j] + lst[k] <= M:
                result = lst[i] + lst[j] + lst[k]
print(result)
