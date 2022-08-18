# 센티와 마법의 뿅망치
import sys
import heapq

input = sys.stdin.readline
N, M, T = map(int, input().split())
heap = []
for _ in range(N):
    heapq.heappush(heap, -int(input()))

count = 0
for _ in range(T):
    v = -heapq.heappop(heap)
    if M > v or v == 1:
        heapq.heappush(heap, -v)
        break
    else:
        heapq.heappush(heap, -(v // 2))
        count += 1

if M > -heap[0]:
    print("YES")
    print(count)
else:
    print("NO")
    print(-int(heap[0]))
