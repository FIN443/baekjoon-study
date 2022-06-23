import heapq
import sys

input = sys.stdin.readline
N = int(input())
min_heap = []
max_heap = []

for _ in range(N):
    num = int(input())

    if len(min_heap) == len(max_heap):
        heapq.heappush(max_heap, -num)
    else:
        heapq.heappush(min_heap, num)

    if min_heap and -max_heap[0] > min_heap[0]:
        min_value = heapq.heappop(min_heap)
        max_value = heapq.heappop(max_heap)
        heapq.heappush(max_heap, -min_value)
        heapq.heappush(min_heap, -max_value)

    print(-max_heap[0])


"""
import heapq
import sys

input = sys.stdin.readline
N = int(input())
heap = []
for _ in range(N):
    num = int(input())
    heapq.heappush(heap, num)
    heap_len = len(heap)
    if heap_len > 2:
        if heap_len % 2 == 1:
            pos = heap_len // 2 + 1
        else:
            pos = heap_len // 2
        temp = heap.copy()
        for i in range(pos):
            num = heapq.heappop(temp)
        print(num)
    else:
        print(heap[0])
"""
