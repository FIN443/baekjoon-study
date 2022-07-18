import heapq
import sys

input = sys.stdin.readline


def dijkstra(start):
    dist = [float("inf") for _ in range(n + 1)]
    dist[start] = 0
    heap = []
    heapq.heappush(heap, (0, start))

    while heap:
        cur_dist, cur_v = heapq.heappop(heap)
        if dist[cur_v] < cur_dist:
            continue

        for to_v, to_dist in graph[cur_v]:
            sum_dist = cur_dist + to_dist
            if dist[to_v] > sum_dist:
                dist[to_v] = sum_dist
                heapq.heappush(heap, (sum_dist, to_v))
    return dist


T = int(input())
for _ in range(T):
    n, m, t = map(int, input().split())  # 교차로, 도로, 목적지 갯수
    s, g, h = map(int, input().split())  # 출발지, g-h로 연결된 교차로 무조건 지나감

    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b, d = map(int, input().split())
        # g-h 또는 h-g로 이어진 정점이 있으면 0.1로 구별
        if (a == g and b == h) or (a == h and b == g):
            d += 0.1
        graph[a].append((b, d))
        graph[b].append((a, d))

    candidate = []
    for _ in range(t):  # 목적지 후보
        candidate.append(int(input()))
    candidate.sort()

    di_s = dijkstra(s)
    for end in candidate:
        if di_s[end] != float("inf") and type(di_s[end]) == float:
            print(end, end=" ")
    print()

    """ 틀린 부분
    di_s = dijkstra(s)
    di_g = dijkstra(g)
    di_h = dijkstra(h)

    result = []
    for end in candidate:
        if (di_s[g] + di_g[h] + di_h[end] == di_s[end]) or (di_s[h] + di_h[g] + di_g[end] == di_s[end]):
            result.append(end)

    result.sort()
    print(*result, sep=" ")
    """
