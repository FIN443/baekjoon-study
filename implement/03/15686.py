# 치킨 배달
from itertools import combinations


N, M = map(int, input().split())
table = []
for _ in range(N):
    table.append(list(map(int, input().split())))

city = []
chicken = []

for i in range(N):
    for j in range(N):
        if table[i][j] == 1:
            city.append((i, j))
        elif table[i][j] == 2:
            chicken.append((i, j))

result = 100000
chicken_lst = combinations(chicken, M)
for v in chicken_lst:
    city_dist = 0
    for j in range(len(city)):
        dist = 100000
        for x, y in v:
            dist = min(dist, abs(x - city[j][0]) + abs(y - city[j][1]))
        city_dist += dist
    result = min(result, city_dist)

print(result)
