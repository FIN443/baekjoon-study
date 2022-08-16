# 맥주 축제
import sys
import heapq

input = sys.stdin.readline
N, M, K = map(int, input().split())
lst = []
heap = []
for _ in range(K):
    v, c = map(int, input().split())
    lst.append((v, c))
lst.sort(key=lambda x: (x[1], x[0]))
cur_c = 0
s = 0
for i in range(K):
    heapq.heappush(heap, lst[i][0])
    s += lst[i][0]
    cur_c = lst[i][1]
    if len(heap) == N:
        if s >= M:
            print(cur_c)
            exit()
        else:
            s -= heapq.heappop(heap)

print(-1)
