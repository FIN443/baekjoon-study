# N번째 큰 수
import sys
import heapq

input = sys.stdin.readline
N = int(input())
heap = []
for _ in range(N):
    lst = list(map(int, input().split()))
    if not heap:
        for i in lst:
            heapq.heappush(heap, i)
    else:
        for i in lst:
            if i > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, i)

print(heap[0])
