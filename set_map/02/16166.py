# 서울의 지하철
import sys
from collections import defaultdict, deque

input = sys.stdin.readline
N = int(input())
train = [[] for _ in range(N)]
station = defaultdict(list)
visited = {}

for i in range(N):
    lst = list(map(int, input().split()))
    for a in lst[1:]:
        train[i].append(a)
        station[a].append(i)
        visited[a] = False

end_station = int(input())
que = deque([(end_station, 0)])

count = 0
result = []
while que:
    cur_v, count = que.popleft()
    if visited[cur_v]:
        continue
    visited[cur_v] = True

    for s in station[cur_v]:
        for to_v in train[s]:
            if to_v == 0:
                result.append(count)
            elif not visited[to_v]:
                que.append((to_v, count + 1))

if result:
    print(min(result))
else:
    print(-1)

"""
3
1 0
2 0 3
2 3 8
8
# 1

3
2 0 9
2 0 3
2 3 8
9
# 0
"""
