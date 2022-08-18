# 세훈이의 선물가게
import sys
import heapq

input = sys.stdin.readline
blue, red, N = map(int, input().split())
heap = []
r_end = b_end = 0
for _ in range(N):
    time, color, cnt = input().split()
    time = int(time)
    cnt = int(cnt)
    if color == "R" and r_end > time:
        time = r_end
    elif color == "B" and b_end > time:
        time = b_end

    order = 0
    while order < cnt:
        if color == "B":
            heapq.heappush(heap, (time + blue * order, "B"))
        else:
            heapq.heappush(heap, (time + red * order, "R"))
        order += 1

    if color == "B":
        b_end = time + blue * order
    else:
        r_end = time + red * order

A = []
B = []
for i in range(len(heap)):
    v, c = heapq.heappop(heap)
    if c == "B":
        A.append(i + 1)
    else:
        B.append(i + 1)

print(len(A))
print(*A, sep=" ")
print(len(B))
print(*B, sep=" ")
