from collections import Counter
import heapq
import sys


input = sys.stdin.readline
heap = []
minus = Counter()

N = int(input())

for _ in range(N):
    num = int(input())
    if num == 0 and not heap:
        print(0)
    elif num == 0 and heap:
        pick = heapq.heappop(heap)
        if minus[pick] > 0:
            print(-pick)
            minus[pick] -= 1
        else:
            print(pick)
    else:
        if num < 0:
            minus[-num] += 1
        heapq.heappush(heap, abs(num))


"""
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
        print(heapq.heappop(heap)[1])
    else:
        heapq.heappush(heap, (abs(num), num))
"""
