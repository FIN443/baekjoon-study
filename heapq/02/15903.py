# 카드 합체 놀이
import sys
import heapq

input = sys.stdin.readline
n, m = map(int, input().split())
heap = list(map(int, input().split()))
heapq.heapify(heap)

for _ in range(m):
    v1 = heapq.heappop(heap)
    v2 = heapq.heappop(heap)
    heapq.heappush(heap, v1 + v2)
    heapq.heappush(heap, v1 + v2)

print(sum(heap))
