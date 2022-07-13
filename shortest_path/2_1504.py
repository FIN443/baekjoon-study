import heapq
import sys


input = sys.stdin.readline
V, E = map(int, input().split())

graph = [[] for _ in range(V + 1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

v1, v2 = list(map(int, input().split()))


def dijkstra(start):
    dist = [float("inf") for _ in range(V + 1)]
    dist[start] = 0
    heap = []
    heapq.heappush(heap, (0, start))
    while heap:
        cur_dist, cur_v = heapq.heappop(heap)
        if dist[cur_v] < cur_dist:
            continue

        for to_v, to_dist in graph[cur_v]:
            updated_dist = cur_dist + to_dist
            if dist[to_v] > updated_dist:
                dist[to_v] = updated_dist
                heapq.heappush(heap, (updated_dist, to_v))
    return dist


d0 = dijkstra(1)  # 시작지점부터 정점까지의 최단거리들
d1 = dijkstra(v1)  # v1지점부터 정점까지의 최단거리들
d2 = dijkstra(v2)  # v2지점부터 정점까지의 최단거리들

result = min(d0[v1] + d1[v2] + d2[V], d0[v2] + d2[v1] + d1[V])  # v1, v2 각각 순서를 바꿔서 들리는 경우
if result != float("inf"):
    print(result)
else:
    print(-1)
