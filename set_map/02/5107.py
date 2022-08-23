# 마니또
from collections import defaultdict, deque

page = 1
while True:
    N = int(input())
    if N == 0:
        break
    graph = defaultdict(list)
    visited = {}
    people = []

    for _ in range(N):
        a, b = input().split()
        graph[a].append(b)
        visited[a] = 0
        people.append(a)

    network = set()
    for idx, i in enumerate(people):
        que = deque([i])
        while que:
            cur_v = que.popleft()
            if visited[cur_v]:
                continue
            visited[cur_v] = idx + 1
            network.add(idx + 1)
            for to_v in graph[cur_v]:
                if not visited[to_v]:
                    que.append(to_v)

    print(f"{page} {len(network)}")
    page += 1
