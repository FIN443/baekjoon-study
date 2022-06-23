import heapq
import sys


input = sys.stdin.readline
heap = []

N = int(input())
for _ in range(N):
    num = int(input())
    if num == 0 and not heap:
        print(0)
    elif num == 0 and heap:
        print(-heapq.heappop(heap))
    else:
        heapq.heappush(heap, -num)
