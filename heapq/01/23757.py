# 아이들과 선물 상자
import sys
import heapq

input = sys.stdin.readline
N, M = map(int, input().split())
heap = list(map(lambda x: -int(x), input().split()))
lst = list(map(int, input().split()))
heapq.heapify(heap)

for i in lst:
    v = -heapq.heappop(heap)
    if v > i:
        heapq.heappush(heap, -(v - i))
    elif v == i:
        pass
    else:
        print(0)
        exit()

print(1)
