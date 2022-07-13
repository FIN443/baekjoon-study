import sys
import heapq

input = sys.stdin.readline
V, E = map(int, input().split())
start = int(input())
dist = [float("inf") for _ in range(V + 1)]  # 시작지점부터 정점까지의 최단 거리
dist[start] = 0  # 시작지점 거리 0
linked = [[] for _ in range(V + 1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    linked[u].append((v, w))

heap = []
heapq.heappush(heap, (0, start))  # heap은 여러개가 들어갈때 맨 앞값을 기준으로 정렬함(중요)

while heap:
    cur_dist, cur_v = heapq.heappop(heap)
    if dist[cur_v] < cur_dist:  # 정점까지의 거리가 저장된 값보다 작으면 continue
        continue

    for to_v, to_dist in linked[cur_v]:  # 연결된 정점들 탐색
        updated_dist = cur_dist + to_dist  # 경로 거리 계산
        if dist[to_v] > updated_dist:  # 목적지 정점의 최단 거리보다 작다면 경로 추가
            dist[to_v] = updated_dist
            heapq.heappush(heap, (updated_dist, to_v))

for i in dist[1:]:
    if i != float("inf"):
        print(i)
    else:
        print("INF")
