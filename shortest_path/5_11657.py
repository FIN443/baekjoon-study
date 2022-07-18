import sys


input = sys.stdin.readline
N, M = map(int, input().split())
graph = []

for _ in range(M):
    a, b, c = map(int, input().split())
    graph.append((a, b, c))


def bellman_ford(start):
    dist = [float("inf") for _ in range(N + 1)]
    dist[start] = 0
    for i in range(1, N + 1):
        for j in range(M):
            cur_v, to_v, cost = graph[j]
            sum_dist = dist[cur_v] + cost
            if dist[cur_v] != float("inf") and dist[to_v] > sum_dist:
                dist[to_v] = sum_dist
                if i == N:  # N번째 노드에서도 값이 갱신되면 negative 사이클이 존재
                    return dist, True

    return dist, False


di_start, inf_cycle = bellman_ford(1)
if inf_cycle:
    print(-1)
else:
    for i in range(2, N + 1):  # 1번 도시부터 2~N번 도시까지 최단 거리 출력
        if di_start[i] == float("inf"):
            print(-1)
        else:
            print(di_start[i])
