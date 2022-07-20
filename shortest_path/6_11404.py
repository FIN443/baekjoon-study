import heapq
import sys


input = sys.stdin.readline
n = int(input())
m = int(input())

# 다익스트라 알고리즘
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


def dijstra(start):
    dist = [float("inf") for _ in range(n + 1)]
    dist[start] = 0
    heap = []
    heapq.heappush(heap, (0, start))
    while heap:
        cur_dist, cur_v = heapq.heappop(heap)
        if cur_dist > dist[cur_v]:
            continue

        for to_v, to_dist in graph[cur_v]:
            sum_dist = cur_dist + to_dist
            if dist[to_v] > sum_dist:
                dist[to_v] = sum_dist
                heapq.heappush(heap, (sum_dist, to_v))

    return dist


for i in range(1, n + 1):
    di = dijstra(i)
    [print(v, end=" ") if v != float("inf") else print(0, end=" ") for v in di[1:]]
    print()


# 플로이드 와샬 알고리즘
table = [[float("inf") for i in range(n + 1)] for j in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    if table[a][b] > c:  # 중복된 값 중에서 작은값으로 갱신
        table[a][b] = c


def floyd_warshall():
    for k in range(1, n + 1):  # 거쳐가는 도시
        for i in range(1, n + 1):  # 출발 도시
            for j in range(1, n + 1):  # 도착 도시
                if i != j and table[i][j] > table[i][k] + table[k][j]:
                    table[i][j] = table[i][k] + table[k][j]


floyd_warshall()
for row in table[1:]:
    for v in row[1:]:
        if v != float("inf"):
            print(v, end=" ")
        else:
            print(0, end=" ")
    print()
